from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import nltk

# Download NLTK resources (first-time run)
nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'GET':
        return jsonify({"message": "Use a POST request to analyze sentiment"}), 405

    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Sentiment score (-1 to 1)

    # Determine sentiment category
    if sentiment_score > 0:
        sentiment = "Positive 😊"
    elif sentiment_score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return jsonify({"sentiment": sentiment, "score": sentiment_score})


if __name__ == '__main__':
    app.run(debug=True)
