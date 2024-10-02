import streamlit as st
import nltk
import pickle
import re

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Loading models
clf = pickle.load(open('clf.pkl', 'rb'))  # Classifier model
tf = pickle.load(open('tfidf.pkl', 'rb'))  # TF-IDF vectorizer

# Preprocessing function (to clean and prepare the text for prediction)
def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)  # Remove all non-word characters (punctuation)
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    return text

# Web App
def main():
    # Custom CSS for the frontend (if needed)
    with open('./Frontend/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Title of the app
    st.title("Resume Screening App")

    # File uploader to allow users to upload a resume in txt or pdf format
    upload_file = st.file_uploader("Upload Resume", type=["txt", "pdf"])

    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode("utf-8")
        except UnicodeDecodeError:
            # If UTF-8 Decoding fails, try with latin-1
            resume_text = resume_bytes.decode("latin-1")

        # Preprocess the resume text
        processed_text = preprocess_text(resume_text)
        
        # Transform the processed text using the TF-IDF vectorizer
        transformed_text = tf.transform([processed_text])
        
        # Make the prediction using the classifier
        predicted_value = clf.predict(transformed_text)
        
        # Display the prediction result
        st.write("Predicted value: ", predicted_value[0])

if __name__ == "__main__":
    main()
