import streamlit as st
import pandas as pd
import joblib
from matplotlib import pyplot



model = joblib.load("disaster_recovery_model.pkl")

# ----------------------------------------------------------
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg, #A8DADC, #457B9D, #BFD7EA);}
.big-font {font-size:32px; color:#1D3557; font-weight:bold;}
.stButton>button {background-color:#457B9D; color:white; border-radius:10px;}
.stButton>button:hover {background-color:#1D3557;}
.stTextInput>div>div>input, .stNumberInput>div>div>input {background:#E0F7FA; border-radius:8px; border:1px solid #A8DADC;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🌊 Blue Pastel Disaster Recovery App</p>', unsafe_allow_html=True)
# -------------------------------------------------

st.title("🌪 Disaster Recovery Days Prediction App")
st.write("Enter disaster details to predict the expected recovery time.")


severity = st.number_input("Severity Index", 0.0, 10.0)
casualties = st.number_input("Casualties", 0, 100000)
economic_loss = st.number_input("Economic Loss (USD)", 0, 100000000)
response_time = st.number_input("Response Time (Hours)", 0.0, 200.0)
aid_amount = st.number_input("Aid Amount (USD)", 0, 100000000)


if st.button("Predict Recovery Days"):
    
    user_input = pd.DataFrame({
        "country": [0],                     
        "disaster_type": [0],               
        "severity_index": [severity],
        "casualties": [casualties],
        "economic_loss_usd": [economic_loss],
        "response_time_hours": [response_time],
        "aid_amount_usd": [aid_amount],
        "response_efficiency_score": [5.0], 
        "latitude": [0.0],                  
        "longitude": [0.0]                  
    })

  
    prediction = model.predict(user_input)
    st.success(f"Estimated Recovery Days: {int(prediction[0])}")


df = pd.read_csv("global_disaster_response_2018_2024 (1).csv")
st.title("🌪 Disaster Recovery Data Visualization ")

# Pastel color palette
pastel_colors = ['#AEC6CF', "#D7FF47", '#77DD77', "#D7A7B2EE"]  # light blue, light orange, light green, light pink

# Create a 2×2 subplot grid
fig = pyplot.figure(figsize=(12, 10))

# 1. Severity vs Recovery Days
pyplot.subplot(2, 2, 1)
pyplot.scatter(df['severity_index'], df['recovery_days'], color=pastel_colors[0])
pyplot.xlabel("Severity Index")
pyplot.ylabel("Recovery Days")
pyplot.title("Severity vs Recovery Days")

# 2. Economic Loss vs Recovery Days
pyplot.subplot(2, 2, 2)
pyplot.scatter(df['economic_loss_usd'], df['recovery_days'], color=pastel_colors[1])
pyplot.xlabel("Economic Loss (USD)")
pyplot.ylabel("Recovery Days")
pyplot.title("Economic Loss vs Recovery Days")

# 3. Response Time vs Recovery Days
pyplot.subplot(2, 2, 3)
pyplot.scatter(df['response_time_hours'], df['recovery_days'], color=pastel_colors[2])
pyplot.xlabel("Response Time (Hours)")
pyplot.ylabel("Recovery Days")
pyplot.title("Response Time vs Recovery Days")

# 4. Aid Amount vs Recovery Days
pyplot.subplot(2, 2, 4)
pyplot.scatter(df['aid_amount_usd'], df['recovery_days'], color=pastel_colors[3])
pyplot.xlabel("Aid Amount (USD)")
pyplot.ylabel("Recovery Days")
pyplot.title("Aid Amount vs Recovery Days")

pyplot.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

