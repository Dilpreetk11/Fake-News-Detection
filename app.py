import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text.lower()

# Prediction function
def predict_news(news_text):
    cleaned = clean_text(news_text)
    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]
    proba = model.predict_proba(vectorized)[0].max() * 100

    label = "✅ Real News" if prediction == 1 else "❌ Fake News"
    if proba < 60:
        return f"{label} (Confidence: {proba:.2f}%) — ⚠️ Low Confidence"
    return f"{label} (Confidence: {proba:.2f}%)"

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection App")
st.write("Enter a news headline or short article and check if it's real or fake.")

user_input = st.text_area("Enter News Text Here:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter some news text to analyze.")
    else:
        prediction = predict_news(user_input)
        st.success(prediction)
