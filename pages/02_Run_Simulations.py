# pages/02_Run_Simulations.py

import streamlit as st

from services.simulation_service import run_simulation

st.title("Run Simulations")

if st.button("Start Simulation"):

    results = run_simulation({})

    st.success("Simulation Complete")

    st.write(results)