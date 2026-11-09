
import streamlit as st

st.title("Set Simulation Parameters")

population_size = st.number_input(
    "Population Size",
    min_value=1,
    value=1000
)

iterations = st.number_input(
    "Iterations",
    min_value=1,
    value=100
)

st.write("Population:", population_size)
st.write("Iterations:", iterations)