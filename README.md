# 📱 Mobile Prices Prediction

A machine learning project for predicting mobile phone prices based on specifications like RAM, memory, brand, battery, and more. This project utilizes data preprocessing, feature engineering, model training, and evaluation, along with a Streamlit app for user interaction.

---

## 🚀 Project Highlights

- Data cleaning and preprocessing using `pandas`
- Feature encoding using `LabelEncoder`
- Model training with:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Evaluation using R² Score and Mean Squared Error (MSE)
- Interactive **Streamlit app** for real-time predictions

---

## 📁 Dataset Overview

The dataset includes features such as:

| Column        | Description                   |
| ------------- | ----------------------------- |
| Brand         | Mobile phone brand            |
| RAM           | Random Access Memory (GB)     |
| Memory        | Internal Storage (GB)         |
| Battery       | Battery capacity (mAh)        |
| Price         | Target variable (in currency) |

---

## 📊 Model Performance

| Model                 | R² Score   |
| ---------------------| ---------- |
| Linear Regression     | ~0.80      |
| Decision Tree         | ~0.89      |
| Random Forest         | ~0.99     |

*Random Forest achieved the best performance.*

---

## 💻 Streamlit App

To run the interactive app:
'''streamlit run app.py'''


## 📂 Project Structure

'''bash
├── prices.ipynb         # Jupyter notebook with full ML pipeline
├── app.py               # Streamlit application
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
'''

## 📌 Future Improvements
I will deploy the model and provide it here 




