# app.py

import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('house_price_model.pkl')

st.title("🏠 House Price Prediction App")
st.markdown("Enter property details below to predict the price.")

# Required field
square_meters = st.number_input("Square Meters (Required)", min_value=20, max_value=500, value=100, step=1)

# Arrange optional fields in two columns
col1, col2 = st.columns(2)

with col1:
    num_rooms = st.slider("Number of Rooms", 1, 10, 3)
    attic = st.slider("Attic Size (m²)", 0, 100, 10)
    garage = st.slider("Garage Size (m²)", 0, 100, 10)

with col2:
    floors = st.slider("Number of Floors", 1, 5, 1)
    basement = st.slider("Basement Size (m²)", 0, 100, 10)
    city_part_range = st.selectbox("City Part Range (1 = Low, 10 = High)", list(range(1, 11)), index=4)

# Binary features in a single row
st.markdown("### Additional Features")
bcol1, bcol2, bcol3, bcol4, bcol5 = st.columns(5)
has_pool = bcol1.checkbox("Pool")
has_yard = bcol2.checkbox("Yard")
is_new = bcol3.checkbox("New")
has_storage = bcol4.checkbox("Storage")
has_storm_protector = bcol5.checkbox("Storm")

# Collect input features
features = np.array([[
    square_meters, num_rooms, floors, attic, basement, garage,
    city_part_range, int(has_pool), int(has_yard), int(is_new),
    int(has_storage), int(has_storm_protector)
]])

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(features)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
