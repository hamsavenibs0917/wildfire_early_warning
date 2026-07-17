import os
import streamlit as st
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

from alert_utils import get_forest_alert
from forest_data import FOREST_OPTIONS, get_searchable_forests
from model_utils import load_model, train_model
from report_utils import generate_report
from weather_utils import fetch_live_weather

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="Wildfire Early Warning", page_icon="🔥", layout="wide")
st.title("🔥 Wildfire Early Warning System")
st.write("Search or choose a forest name so the app can fetch live weather details and predict the forest department alert.")

search_term = st.text_input("Search Forest", value="")
filtered_forests = get_searchable_forests(search_term)

if not filtered_forests:
    st.warning("No forest found. Try another search term.")
    filtered_forests = FOREST_OPTIONS

selected_forest = st.selectbox(
    "Choose Forest",
    filtered_forests,
    format_func=lambda forest: f"{forest['name']} - {forest['state']}",
)

st.info(
    f"Selected Forest: {selected_forest['name']} | State: {selected_forest['state']} | "
    f"Lat: {selected_forest['latitude']} | Lon: {selected_forest['longitude']}"
)

if st.button("Get Live Weather and Forest Alert"):
    model = load_model()

    if model is None:
        try:
            model, accuracy = train_model()
            st.success(f"Model trained automatically. Accuracy: {accuracy:.2f}")
        except Exception as error:
            st.error(f"Could not train the model automatically: {error}")
            model = None

    if model is not None:
        try:
            selected_latitude = selected_forest["latitude"]
            selected_longitude = selected_forest["longitude"]
            weather = fetch_live_weather(selected_latitude, selected_longitude)
            values = pd.DataFrame([
                {
                    "temperature": weather["temperature"],
                    "humidity": weather["humidity"],
                    "wind_speed": weather["wind_speed"],
                    "rainfall": weather["rainfall"],
                }
            ])

            prediction = int(model.predict(values)[0])
            risk = "HIGH" if prediction == 1 else "LOW"
            alert_level, action = get_forest_alert(weather, risk)
            report = generate_report(weather, risk)

            st.session_state["prediction"] = {
                "risk": risk,
                "alert_level": alert_level,
                "action": action,
                "report": report,
                "input": weather,
                "source": "Open-Meteo live weather",
                "location": selected_forest,
                "forest_name": selected_forest["name"],
            }
        except requests.RequestException:
            st.error("Could not fetch live weather data. Check your internet connection and try again.")

result = st.session_state.get("prediction")

if result:
    st.subheader(f"Current Forest Department Alert: {result['alert_level']}")
    st.write(f"Risk Level: {result['risk']}")
    st.write(f"Weather Source: {result.get('source', 'live weather')}")
    st.write(f"Forest Name: {result.get('forest_name', selected_forest['name'])}")
    location = result.get("location", {})
    if isinstance(location, dict):
        st.write(f"Matched Location: {location.get('name', '')}")
        st.write(f"Latitude: {location.get('latitude', '')}")
        st.write(f"Longitude: {location.get('longitude', '')}")
    weather = result.get("input", {})
    st.write(f"Temperature: {weather.get('temperature', '')} °C")
    st.write(f"Humidity: {weather.get('humidity', '')} %")
    st.write(f"Wind Speed: {weather.get('wind_speed', '')} km/h")
    st.write(f"Rainfall: {weather.get('rainfall', '')} mm")
    st.info(result["action"])
    st.write(result["report"])
else:
    st.info("Press Get Live Weather and Forest Alert to see the output.")
