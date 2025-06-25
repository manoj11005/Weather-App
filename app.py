import streamlit as st
from utils import get_weather_data, format_weather_data

st.set_page_config(page_title="Weather Dashboard", page_icon="⛅")
st.title("🌤️ Real-Time Weather Dashboard")

city = st.text_input("Enter City Name:", "Delhi")

if st.button("Get Weather"):
    data = get_weather_data(city)
    weather = format_weather_data(data)

    if weather:
        st.success(f"Weather for {weather['City']}")
        st.write(f"🌡️ Temperature: {weather['Temperature (°C)']} °C")
        st.write(f"🤗 Feels Like: {weather['Feels Like (°C)']} °C")
        st.write(f"💧 Humidity: {weather['Humidity (%)']}%")
        st.write(f"📊 Pressure: {weather['Pressure (hPa)']} hPa")
        st.write(f"💨 Wind Speed: {weather['Wind Speed (m/s)']} m/s")
        st.write(f"🌥️ Condition: {weather['Weather']}")
    else:
        st.error("City not found or API error.")