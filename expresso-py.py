from flask import Flask, request, Response
import nltk, re, json
app = Flask(__name__)

# main page route to check server status
@app.route("/")
def main():
	return "Server is up and running"

# route to do NLP analysis on submitted texts
@app.route("/analyze-text", methods=["POST"])
def analyzeText():
	if request.method == "POST":
		
		# load json with data into a python dictionary
		data = json.loads(request.data)

		# extract text tokens (words and punctuation)
		tokens = nltk.word_tokenize(data["text"])

		# extract just words from tokens
		nonPunct = re.compile('.*[A-Za-z0-9].*')
		wordTokens = [w for w in tokens if nonPunct.match(w)]

		# count number of words
		data["wordCount"] = len(wordTokens)

		# send back analysis results as a json
		resp = Response(response=json.dumps(data), status=200, mimetype="application/json")
		return resp

if __name__ == "__main__":
	app.run(debug=True)