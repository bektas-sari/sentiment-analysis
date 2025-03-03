# Sentiment Analysis

## Overview
Sentiment Analysis is a Flask-based web application that analyzes the sentiment of user-provided text using Natural Language Processing (NLP) techniques. It utilizes **TextBlob** for polarity detection and provides real-time sentiment classification (Positive, Neutral, Negative).

## Features
- Simple and modern UI
- Sentiment analysis using **TextBlob**
- Flask-powered REST API
- Responsive and interactive interface
- Animated UI effects for better user experience

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bektas-sari/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open in your browser:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
├── static/
│   ├── style.css  # Styling for UI
│   ├── script.js  # JavaScript logic
├── templates/
│   ├── index.html # Main UI
├── app.py         # Flask API
├── requirements.txt # Dependencies
```

## Technologies Used
- **Flask** (Backend API)
- **TextBlob** (Sentiment Analysis)
- **HTML, CSS, JavaScript** (Frontend)

## Author
**Bektas Sari**  
📧 Contact: bektas.sari@gmail.com  
🔗 GitHub: [bektas-sari](https://github.com/bektas-sari)

## License
This project is licensed under the MIT License.
