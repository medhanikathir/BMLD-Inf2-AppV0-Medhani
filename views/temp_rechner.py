import streamlit as st
from functions.temperatur import celsius_to_fahrenheit

st.title("Temperaturrechner")

st.write("Geben Sie eine Temperatur in Celsius ein, um sie in Fahrenheit umzuwandeln.")

with st.form("temp_form"):
    celsius = st.number_input("Temperatur in Celsius", value=0.0)
    submit_button = st.form_submit_button("Umrechnen")
    if submit_button:
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius} °C entspricht {fahrenheit} °F.")

