# 📧 Spam Message Classification System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?style=flat-square&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A Machine Learning and NLP-powered web application that automatically classifies SMS messages as **Spam** or **Not Spam** in real time.

---

## 🚀 Project Overview

The Spam Message Classification System analyzes SMS text using a trained Naive Bayes model and delivers instant predictions through a lightweight Flask web interface. Built as a beginner-friendly end-to-end AI project — from raw data to deployed web app.

---

## 🎯 Objective

- Automatically detect spam messages using Machine Learning
- Apply NLP techniques for text preprocessing and feature extraction
- Train and evaluate a Multinomial Naive Bayes classifier
- Deploy the model through a Flask web application

---

## 🧠 Technologies Used

| Category | Tools |
|---|---|
| Language | Python 3.8+ |
| Machine Learning | Scikit-learn, Multinomial Naive Bayes |
| NLP | NLTK (tokenization, stopwords, lemmatization) |
| Web Framework | Flask |
| Data Processing | Pandas, CountVectorizer |
| Model Persistence | Joblib |
| Frontend | HTML, CSS |

---

## 📂 Project Structure

```
Spam-Classification-Model/
│
├── app.py                   # Flask web application
├── preprocessing.py         # NLP text cleaning utilities
├── model training.ipynb     # Jupyter notebook for model training
├── spam.csv                 # SMS Spam Collection Dataset
├── requirements.txt         # Python dependencies
├── README.md
│
├── models/
│   ├── spam_classifier.pkl  # Trained Naive Bayes model
│   └── count_vectorizer.pkl # Fitted CountVectorizer
│
├── templates/
│   └── index.html           # Web interface
│
└── static/
    └── style.css            # Stylesheet
```

---

## 📊 Dataset Information

This project uses the [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection).

| Column | Description |
|---|---|
| `v1` | Message label (`ham` / `spam`) |
| `v2` | SMS message text |

**Example:**

```
v1,v2
ham,Hello how are you?
spam,Free entry in a weekly competition!
```

**Label Encoding:**

| Label | Encoding | Meaning |
|---|---|---|
| `ham` | 0 | Normal message |
| `spam` | 1 | Spam message |

> Only `v1` and `v2` columns are used. Extra empty columns in the CSV are ignored during training.

---

## ⚙️ System Workflow

```
Raw SMS Data
     │
     ▼
Text Preprocessing (NLP)
  ├─ Lowercase conversion
  ├─ Remove punctuation & numbers
  ├─ Remove stopwords
  └─ Lemmatization
     │
     ▼
Feature Extraction
  └─ CountVectorizer (Bag of Words)
     │
     ▼
Model Training
  └─ Multinomial Naive Bayes
     │
     ▼
Model Saved (.pkl)
     │
     ▼
Flask Web App → Predict New Messages
```

---

## 🤖 Machine Learning Model

**Algorithm:** Multinomial Naive Bayes

**Why this model?**
- Highly efficient for text classification tasks
- Fast training and real-time prediction
- Performs well with word frequency (Bag of Words) features
- Industry-standard algorithm for spam filtering systems

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/spam-classification-model.git
cd spam-classification-model
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

Run once to generate the saved model files:

```bash
python train_model.py
```

This will create:
```
models/spam_classifier.pkl
models/count_vectorizer.pkl
```

### 5. Run the Flask Application

```bash
python app.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

---

## 🌐 How to Use

1. Open the web application in your browser
2. Enter any SMS message into the input box
3. Click **Predict**
4. The system will instantly display the result:

| Result | Meaning |
|---|---|
| ✅ **Not Spam** | The message appears to be legitimate |
| ❌ **Spam** | The message has been flagged as spam |

---

## ✅ Features

- NLP-based text cleaning pipeline
- Machine Learning classification (Naive Bayes)
- Real-time prediction via web interface
- Lightweight, fast, and easy to deploy
- Beginner-friendly end-to-end AI project

---

## 🔮 Future Improvements

- [ ] Upgrade to TF-IDF Vectorization for better feature representation
- [ ] Experiment with Deep Learning models (LSTM, BERT)
- [ ] Display prediction confidence score
- [ ] Deploy to cloud (Render, Heroku, or AWS)
- [ ] Support multi-language spam detection

---

## 👨‍💻 Author

**Mohammed Jasir**  
AI & Machine Learning Enthusiast

---

