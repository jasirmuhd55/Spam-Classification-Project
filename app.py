# app.py
from flask import Flask, render_template, request
import joblib
from preprocessing import clean_text

app = Flask(__name__)

# Load models
model = joblib.load('Spam-Classification-Model-main\models\spam_classifier.pkl')
vectorizer = joblib.load('Spam-Classification-Model-main\models\count_vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    user_input = ""
    if request.method == 'POST':
        user_input = request.form['message']
        cleaned = clean_text(user_input)
        features = vectorizer.transform([cleaned])
        result = model.predict(features)[0]
        prediction = "Spam ❌" if result == 1 else "Not Spam ✅"
    return render_template('index.html', prediction=prediction, user_input=user_input)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)