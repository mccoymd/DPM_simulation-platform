# pages/01_Dashboard.py

import streamlit as st

from services.patient_service import (
    load_patients
)

patients = load_patients()

total_patients = len(patients)

total_simulations = sum(
    len(p["simulations"])
    for p in patients
)

total_queries = sum(
    len(p["queries"])
    for p in patients
)

total_analyses = sum(
    len(p["analyses"])
    for p in patients
)

st.title("Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Patients",
    total_patients
)

c2.metric(
    "Simulations",
    total_simulations
)

c3.metric(
    "Queries",
    total_queries
)

c4.metric(
    "Analyses",
    total_analyses
)

st.divider()

st.subheader("Patients")

for patient in patients:

    st.write(
        f"{patient['patient_id']} | "
        f"{patient['cancer_type']}"
    )