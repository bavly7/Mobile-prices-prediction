import pickle
import numpy as np
import streamlit as st

# Load the model
try:
    with open(r'D:\Gam3a\for_me\Project_Phones\mobile_predictions5.sav', 'rb') as file:
        model = pickle.load(file)

    if not hasattr(model, "predict"):
        st.error("🔴 The loaded model does not have a 'predict' function. Ensure you're loading the correct model.")
        st.stop()

except FileNotFoundError:
    st.error("🔴 Model file 'mobile_predictions.sav' not found! Please place it in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"🔴 Error loading model: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="📱 Mobile Price Prediction", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    /* General app background */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }

    /* Headers and general text color */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: black;  /* Headers in black */
    }
    .stMarkdown p, .stMarkdown div {
        color: black;  /* General text in black */
    }

    /* Input labels (selectbox, slider, etc.) */
    .stSelectbox label, .stSlider label {
        color: black !important;  /* Force labels to be black */
    }

    /* Title styling */
    h1 {
        color: black !important;  /* Force title to be black */
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.title("📱 Mobile Price Prediction")
st.markdown("---")
st.markdown("### 🛠️ Customize Your Mobile Features")

# User Inputs
st.markdown("#### 🔋 Battery Capacity (mAh)")
battery_options = [1000,5000, 4500, 4000, 6000, 5200, 4300, 5100, 4600, 5500, 4800, 4400, 4700, 4200, 5050, 3700, 8040, 3200, 3500, 5800, 9510]
battery_capacity = st.selectbox("Select Battery Capacity", battery_options, key="battery_selectbox")

st.markdown("#### 🧠 RAM (GB)")
ram_options = [4,8, 6, 12, 4, 3, 16, 2, 1, 10]
ram = st.selectbox("Select RAM", ram_options, key="ram_selectbox")

st.markdown("#### ⚙️ Processor")
processor_options = [
    "Snapdragon 8 Gen 2", "MediaTek Dimensity 810", "MediaTek Helio G99", "Snapdragon 8 Gen 3",
    "MediaTek Helio G85", "A16 Bionic", "A15 Bionic", "Snapdragon 8 Gen 1", "Qualcomm Snapdragon 695",
    "MediaTek Dimensity 700", "MediaTek Dimensity 8200", "MediaTek Helio G80", "A14 Bionic",
    "Snapdragon 8+ Gen 1", "A13 Bionic", "MediaTek Helio G88", "Snapdragon 765G", "MediaTek Dimensity 9200",
    "MediaTek Dimensity 9000", "A12 Bionic",
    "Dimensity 1100", "Snapdragon 617", "Kirin 990E 5G", "Kirin 9000 5G", "Exynos 7570",
    "Snapdragon 425", "Exynos 7870", "Snapdragon 450", "Snapdragon 480+", "Snapdragon 626",
    "Snapdragon 730G", "Qualcomm Snapdragon 480", "MediaTek Helio P22", "MediaTek G99",
    "Snapdragon 615", "Snapdragon 439", "Snapdragon 652", "MediaTek Helio G35", "MediaTek MT6592",
    "MediaTek Dimensity 8400","Mate X2"
]
processor = st.selectbox("Select Processor", processor_options, key="processor_selectbox")
st.markdown("#### 📸 Front Camera (MP)")
front_camera_options = [1,2,3,18,20,16, 32, 8, 12, 5, 13, 50, 10, 7, 2, 20, 11, 60, 68, 44, 24, 14, 25, 28, 48]
front_camera = st.selectbox("Select Front Camera", front_camera_options, key="front_camera_selectbox")

st.markdown("#### 📷 Back Camera (MP)")
back_camera_options = [1,2,3,4,50, 13, 64, 48, 108, 52, 60, 58, 8, 24, 36, 62, 12, 74, 16, 66, 150, 15, 22, 5]
back_camera = st.selectbox("Select Back Camera", back_camera_options, key="back_camera_selectbox")

# Encode Processor (convert to numerical value)
processor_mapping = {processor: idx for idx, processor in enumerate(processor_options)}
processor_encoded = processor_mapping[processor]

# Create input array for prediction
input_features = np.array([
    battery_capacity,
    ram,
    processor_encoded,
    front_camera,
    back_camera
]).reshape(1, -1)  # Reshape for model input

# Predict Button
st.markdown("---")
if st.button('Predict Price', key='predict_button'):
    try:
        prediction = model.predict(input_features)
        st.success(f'💰 The predicted price is: **${prediction[0]:,.2f}**')
    except Exception as e:
        st.error(f"🔴 Error during prediction: {e}")

# Footer
st.markdown("---")
st.markdown("### 📊 **About the Model**")
st.markdown("This model predicts the price of mobile phones based on **Battery Capacity**, **RAM**, **Processor**, **Front Camera**, and **Back Camera**.")
st.markdown("---")
st.markdown("### 📝 **Note**")
st.markdown("The predicted price is an estimate and may vary based on market conditions and other factors.")