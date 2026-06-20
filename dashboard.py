import streamlit as st
import pandas as pd

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

st.title("🌍 Air Quality Monitoring Dashboard")

data = pd.read_csv("air_quality.csv")

# Statistics
col1, col2, col3 = st.columns(3)

col1.metric("Average AQI", round(data["AQI"].mean(), 2))
col2.metric("Maximum AQI", data["AQI"].max())
col3.metric("Minimum AQI", data["AQI"].min())

st.subheader("Air Quality Data")
st.dataframe(data)

st.subheader("AQI Comparison")
st.bar_chart(data.set_index("City")["AQI"])

st.subheader("Temperature Comparison")
st.line_chart(data.set_index("City")["Temperature"])

st.subheader("Humidity Comparison")
st.line_chart(data.set_index("City")["Humidity"])

st.subheader("Search City")
city = st.selectbox("Choose City", data["City"])
st.write(data[data["City"] == city])

st.subheader("Air Quality Status")

for i in range(len(data)):
    city_name = data.loc[i, "City"]
    aqi = data.loc[i, "AQI"]

    if aqi <= 100:
        status = "🟢 Good"
    elif aqi <= 200:
        status = "🟡 Moderate"
    else:
        status = "🔴 Poor"

    st.write(f"{city_name}: {status}")