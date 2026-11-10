import streamlit as st

from services.patient_service import (
    load_patients,
    add_simulation,
    add_query,
    add_analysis
)

patients = load_patients()

st.title(
    "Patient Workspace"
)

if not patients:

    st.info(
        "No patients found."
    )

    st.stop()

selected_patient = st.selectbox(
    "Select Patient",
    patients,
    format_func=lambda p:
        p["patient_id"]
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Overview",
        "Simulations",
        "Queries",
        "Analyses"
    ]
)

with tab1:

    st.subheader(
        selected_patient["patient_id"]
    )

    st.write(
        f"Cancer Type: "
        f"{selected_patient['cancer_type']}"
    )

    st.write(
        f"Simulations: "
        f"{len(selected_patient['simulations'])}"

    )

    st.write(
        f"Queries: "
        f"{len(selected_patient['queries'])}"
    )

    st.write(
        f"Analyses: "
        f"{len(selected_patient['analyses'])}"
    )

with tab2:
    st.subheader(
        "Simulation History"
    )

    st.write(
        selected_patient["simulations"]
    )
    st.divider()
    simulation_name = st.text_input(
        "Simulation Name",
        key="simulation_name"
    )

    if st.button(
        "Add Simulation",
        key="add_sim_button"
    ):

        add_simulation(
            selected_patient["patient_id"],
            simulation_name
        )

        st.rerun()


with tab3:

    st.subheader(
        "Query History"
    )

    st.write(
        selected_patient["queries"]
    )

    st.divider()

    query_name = st.text_input(
        "Query Name",
        key="query_name"
    )

    if st.button(
        "Add Query",
        key="add_query_button"
    ):

        add_query(
            selected_patient["patient_id"],
            query_name
        )

        st.rerun()

with tab4:

    st.subheader(
        "Analysis History"
    )

    st.write(
        selected_patient["analyses"]
    )
    st.divider()

    analysis_name = st.text_input(
        "Analysis Name",
        key="analysis_name"
    )

    if st.button(
        "Add Analysis",
        key="add_analysis_button"
    ):

        add_analysis(
            selected_patient["patient_id"],
            analysis_name
        )

        st.rerun()