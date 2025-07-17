# # Fake News Detection System

This Streamlit app classifies news text as "Real News" or "Fake News" using a pre-trained machine learning model.

## Features

* Input news text.
* Get "Real" or "Fake" classification with confidence.

---

## Setup

1.  **Files:** Place `app.py`, `model.pkl`, `tfidf_vectorizer.pkl`, `README.md`, and `requirements.txt` in one folder.
2.  **Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # Windows: `venv\Scripts\activate`
    ```
3.  **Install:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1.  Ensure `model.pkl` and `tfidf_vectorizer.pkl` are in the same directory.
2.  Run the app:
    ```bash
    streamlit run app.py
    ```
3.  Open in browser (usually `http://localhost:8501`).

---

## Important Files

* `model.pkl`: Your trained ML model.
* `tfidf_vectorizer.pkl`: Your text vectorizer.
    *These files are crucial and must be present.*
