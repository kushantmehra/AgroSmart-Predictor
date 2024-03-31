import streamlit as st
import pickle

# Load the trained model
model_filename = 'model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# Define the Streamlit app UI
st.title('AgroSmart Predictor')

# Input fields for user to enter data
N = st.slider('Nitrogen (N)', min_value=0, max_value=2000, value=100)
P = st.slider('Phosphorous (P)', min_value=0, max_value=1000, value=50)
K = st.slider('Potassium (K)', min_value=0, max_value=2000, value=100)
temperature = st.slider('Temperature (°C)', min_value=0.0, max_value=150.0, value=25.0)
humidity = st.slider('Humidity (%)', min_value=0.0, max_value=110.0, value=50.0)
ph = st.slider('pH Level', min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.slider('Rainfall (mm)', min_value=0.0, max_value=1500.0, value=250.0)

# Button to trigger predictions
if st.button('Predict'):
    # Prepare input data
    data = [[N, P, K, temperature, humidity, ph, rainfall]]
    # Make predictions
    prediction = model.predict(data)
    # Display the predicted crop
    st.success(f'Predicted Crop: {prediction[0]}')
