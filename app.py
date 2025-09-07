import streamlit as st
import nltk
import pickle
import string

# import stopwords
from nltk.corpus import stopwords
import ssl
import certifi
import nltk

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

import ssl
import nltk

# Fix SSL issues on macOS
ssl._create_default_https_context = ssl._create_unverified_context

# Ensure punkt resources are available
for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)


# Data preprocessing

def text_preprocessing(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []

  for i in text:
    if i.isalnum():
      y.append(i)

  text = y.copy()
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)



tdift = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/sms spam classifier")

sms_input = st.text_area("Enter the sms or Email to check")


if st.button("predict"):

  #1. preprocessing

  transform_text = text_preprocessing(sms_input)


  #2. vectorize
  vector_input = tdift.transform([transform_text])

  #3. model prdiction

  result = model.predict(vector_input)[0]

  if result == 0:
      st.success('Not a spam SMS/EMAIL')
  else:
      st.warning('Its a spam SMS/EMAIL', icon="🚨")

