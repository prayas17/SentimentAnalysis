from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize Flask app
app = Flask(__name__)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to preprocess text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    
    # Tokenization (split the text into words/tokens)
    tokens = nltk.word_tokenize(text)
    
    # Remove punctuation
    tokens = [word for word in tokens if word.isalnum()]
    
    # Remove stopwords
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Join tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    # Get user input from POST request
    user_input = request.form.get('text')
    
    # Preprocess the input text
    preprocessed_input = preprocess_text(user_input)
    
    # Analyze sentiment using VADER
    sentiment_scores = analyzer.polarity_scores(preprocessed_input)
    
    # Determine overall sentiment
    if sentiment_scores['compound'] >= 0.05:
        overall_sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"
    
    # Prepare response
    response = {
        "input_text": user_input,
        "sentiment": overall_sentiment
    }
    
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
