import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import pydeck as pdk
import plotly.express as px

st.title("Analytics")

#st.markdown("# Page 1 ❄️")

#Sidebar settings
st.sidebar.markdown("Analytics")


# -------------------------------
# Passenger Flow Analytics
# -------------------------------

st.subheader("📊 Passenger Flow Analytics")
df = pd.DataFrame({
    "Hour": list(range(6, 22)),
    "Passengers": [30, 50, 90, 120, 150, 170, 200, 180, 160, 140, 100, 80, 60, 50, 40, 30]
})
chart = alt.Chart(df).mark_area(opacity=0.4).encode(
    x="Hour",
    y="Passengers"
)
st.altair_chart(chart, use_container_width=True)

# -------------------------------
# Passenger Flow Analytics
# -------------------------------
st.subheader("📊 Passenger Flow Analytics")

# Filters
bus_line = st.selectbox("Select Bus Line", ["Route A", "Route B", "Route C"])
stop = st.selectbox("Select Stop", ["All", "Piazza Dante", "Via Verdi", "Università Centrale"])

# Dummy analytics
df = pd.DataFrame({
    "Hour": range(6, 24),
    "Passengers": [10, 15, 30, 45, 60, 80, 100, 85, 70, 50, 40, 30, 20, 15, 10, 5, 3, 2]
})

st.bar_chart(df.set_index("Hour"))

# -------------------------------
# 📽️ Animated Passenger Flow by Route and Hour
# -------------------------------
st.subheader("📽️ Animated Passenger Flow by Route and Hour")

# Dummy data for animation
data = {
    "Route": ["A", "B", "C"] * 10,
    "Hour": sum([[str(h)] * 3 for h in range(6, 16)], []),  # 6 to 15
    "Passengers": [
        30, 20, 15,
        45, 25, 20,
        60, 40, 30,
        80, 60, 45,
        100, 70, 60,
        120, 90, 75,
        140, 110, 90,
        130, 100, 85,
        110, 90, 70,
        90, 70, 60
    ]
}
df_anim = pd.DataFrame(data)

fig = px.bar(
    df_anim,
    x="Passengers", y="Route", color="Route",
    animation_frame="Hour",
    orientation="h",
    range_x=[0, 160],
    title="Passenger Load per Route Over Time",
    labels={"Passengers": "Number of Passengers", "Route": "Bus Route"}
)

st.plotly_chart(fig, use_container_width=True)
