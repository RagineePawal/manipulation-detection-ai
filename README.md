# manipulation-detection-ai
AI-powered NLP system for real-time psychological manipulation detection.
# 🧠 Real-Time Psychological Manipulation Detection in Digital Communication

AI-powered NLP system for detecting psychological manipulation and persuasion techniques in digital communication platforms.

## 🚀 Overview

This project detects manipulative intent in messages using Machine Learning and NLP techniques.

The system performs:

- Intent Detection
- Manipulation Type Classification
- Domain Detection
- Severity Estimation
- Confidence Scoring

The project is designed for:

- Cybersecurity platforms
- Social media moderation
- Telegram monitoring
- Online safety systems
- Real-time communication analysis

---

# 🏗️ System Features

 Real-time detection  
 Multi-label classification  
 Lightweight ML pipeline  
 Explainable outputs  
 FastAPI backend  
 Telegram bot integration  
 Structured JSON responses  
 Low latency inference  

---

# Technologies Used

## Backend
- Python
- FastAPI

## Machine Learning
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorization

## NLP
- NLTK
- Regex
- Word N-grams
- Character N-grams

## Deployment
- Telegram Bot API
- Joblib
- Uvicorn

---

#  Dataset

Synthetic dataset created using structured templates for:

- Neutral conversations
- Emotional manipulation
- Authority pressure
- Urgency tactics
- Guilt-based persuasion

Domains covered:
- Workplace
- Social media
- Personal communication
- Financial scams

---

#  Workflow

1. Input message received
2. Text preprocessing
3. TF-IDF feature extraction
4. Parallel ML classifiers run
5. Intent + type + severity prediction
6. Structured JSON output generated

---

# System Architecture

## Input Layer
- REST API
- Telegram Bot
- CLI Tools

## Feature Engineering
- TF-IDF
- Word N-grams
- Character N-grams

## Prediction Layer
- Intent Model
- Type Model
- Domain Model
- Severity Model

## Output Layer
- JSON response
- Confidence scores
- Human-readable labels

---

# Sample Output

```json
{
  "intent": "coercive",
  "type": "emotional_blackmail",
  "domain": "personal",
  "severity": "high",
  "confidence": 0.91
}
```

---

# ML Model

Algorithm Used:
- Logistic Regression

Why?
- Fast inference
- High interpretability
- Efficient on sparse TF-IDF features
- Suitable for real-time systems

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- Macro F1 Score
- Weighted F1 Score

---

#  API Endpoints

## Health Check

```bash
GET /health
```

## Predict Manipulation

```bash
POST /predict
```

Request:

```json
{
  "message": "If you really care about us, you'll do this."
}
```

---

# Run Locally

## Clone Repository

```bash
git clone https://github.com/yourusername/manipulation-detection-ai.git
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app:app --reload
```

---

# Telegram Bot

The Telegram bot allows real-time monitoring of messages and instant manipulation analysis.

Features:
- Live message detection
- Confidence scoring
- Label generation
- JSON response support

---

# Future Improvements

- Real-world conversational datasets
- Lightweight transformer models
- Voice transcript analysis
- Browser extension support
- Multilingual manipulation detection

---

# Contributors

- Raginee Pawal
- Tanishka Patil
- Vedika Dawani
- Vineet Dorikar
- Shubham Sahu

---

# 📜 License

MIT License
