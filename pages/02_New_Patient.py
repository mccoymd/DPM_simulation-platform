# pages/02_New_Patient.py

import streamlit as st

from services.patient_service import (
    create_patient
)

st.title(
    "Create Patient"
)

patient_id = st.text_input(
    "Patient ID"
)

cancer_type = st.selectbox(
    "Cancer Type",
    [
        "NSCLC",
        "Breast",
        "Colon",
        "Melanoma",
        "Other"
    ]
)

if st.button("Create Patient"):

    create_patient(
        patient_id,
        cancer_type
    )

    st.success(
        "Patient created."
    )