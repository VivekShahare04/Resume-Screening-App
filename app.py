import streamlit as st
import nltk
import pickle
import re

nltk.download('punkt')
nltk.download('stopwords')

#loading models
clf = pickle.load(open('clf.pkl','rb'))
tf = pickle.load(open('tfidf.pkl','rb'))

#Web App
def main():
    with open('./Frontend/style.css') as f:
        st.markdown(f'<style>{f.read()}</style',unsafe_allow_html=True)
        
    st.title("Resume Screening App")
    upload_file = st.file_uploader("Upload Resume",type=["txt","pdf"])
    
    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode("utf-8")
        except UnicodeDecodeError:
            # if UTF-8 Decoding fails try with latin-1
            resume_text = resume_bytes.decode("latin-1")

        st.write("predicted_value")

        
if __name__=="__main__":
    main()
