# Fake-News-Detection
This project provides a simple yet effective web application to detect fake news using a pre-trained machine learning model. Built with Streamlit, it offers an intuitive interface where users can input news text and instantly get a prediction on whether it's real or fake, along with a confidence score.

Features
Real-time Prediction: Instantly classify news headlines or articles as "Real News" or "Fake News."
Confidence Score: Displays the prediction confidence, helping users gauge the reliability of the classification.
Text Preprocessing: Includes a built-in text cleaning function to prepare input data for the model.
User-Friendly Interface: Powered by Streamlit for an easy-to-use web application.

Tech Stack
Python 3.x
Streamlit: For building the interactive web application.
Joblib: For loading the pre-trained machine learning model and TF-IDF vectorizer.
Scikit-learn: (Implicitly used for model training and TF-IDF vectorization) The underlying library for the saved model.pkl and tfidf_vectorizer.pkl.


