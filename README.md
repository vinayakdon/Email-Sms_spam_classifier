# 📧📱 Email & SMS Spam Classifier  

A machine learning project to classify whether a given **email or SMS message** is **spam** or **not spam**. This project leverages **text preprocessing, vectorization, and classification models**, with a focus on **Naive Bayes** due to its strong performance in text-related tasks.  

---

## 🔍 Project Overview  
- Built a classifier that detects spam messages using **machine learning**.  
- Tried multiple algorithms and selected **Naive Bayes**, as it provided the best balance of performance based on **precision score** (preferred over accuracy due to dataset imbalance).  
- Applied **Count Vectorization** and **TF-IDF Vectorization** for text representation.  
- Performed **EDA (Exploratory Data Analysis)** to understand dataset properties and message distributions.  

---

## 📊 Dataset  
- Dataset sourced from **Kaggle** (SMS/Email spam dataset).  

---

## ⚙️ Tech Stack  
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK  
- **Vectorization:** CountVectorizer, TfidfVectorizer  
- **Model:** Naive Bayes (tested other algorithms as well)  
- **Deployment/UI:** Streamlit, FastAPI  

---

## ✨ Features  
- User can input a text message in a **Streamlit web app**.  
- Model classifies the message as **Spam** or **Not Spam**.  
- Displays **classification metrics** such as accuracy and precision.  
- Visualizes insights from the dataset (EDA).  

---

## 🤖 Model Details  
- **Naive Bayes Classifier** was chosen for the final implementation.  
- Tested with other ML algorithms for comparison.  
- Evaluation metrics included:  
  - Accuracy Score  
  - Precision Score (used as primary metric due to dataset quality/imbalance).  

---

## 📈 Performance  
- Achieved strong **accuracy** and **precision** scores.  
- Naive Bayes outperformed other models in handling text classification.  

---

## 🚀 How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/vinayakdon/Email-Sms_spam_classifier.git
   cd Email-Sms_spam_classifier
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
---

## 📸 Screenshots  
(Add screenshots of the app UI here after running the project.)  

---

## 🔮 Future Improvements  
- Support classification in **multiple languages**.  
- Enhance dataset with **real-time email/SMS feeds**.  
- Deploy on **cloud platforms** (Heroku, AWS, etc.) for global accessibility.  
- Experiment with **deep learning models** (RNNs, LSTMs, Transformers) for better accuracy.  
- Add **explainability** features (e.g., highlighting words contributing most to spam detection).  

---

## 👨‍💻 Author  
**Vinayak Donawad**  
- [LinkedIn](https://www.linkedin.com/in/vinayak-donawad-a018171b8/)  
- [GitHub](https://github.com/vinayakdon)  

---


