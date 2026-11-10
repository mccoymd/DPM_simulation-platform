import json
from pathlib import Path

DATA_FILE = Path("data/patients.json")


def load_patients():

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_patients(patients):

    with open(DATA_FILE, "w") as f:
        json.dump(
            patients,
            f,
            indent=2
        )


def create_patient(
    patient_id,
    cancer_type
):

    patients = load_patients()

    patient = {

        "patient_id": patient_id,

        "cancer_type": cancer_type,

        "simulations": [],

        "queries": [],

        "analyses": []
    }

    patients.append(patient)

    save_patients(patients)

    return patient


def add_simulation(
    patient_id,
    simulation_name
):

    patients = load_patients()

    for patient in patients:

        if patient["patient_id"] == patient_id:

            patient[
                "simulations"
            ].append(
                {
                    "name":
                    simulation_name
                }
            )

    save_patients(patients)


def add_query(
    patient_id,
    query_name
):

    patients = load_patients()

    for patient in patients:

        if patient["patient_id"] == patient_id:

            patient[
                "queries"
            ].append(
                {
                    "name":
                    query_name
                }
            )

    save_patients(patients)


def add_analysis(
    patient_id,
    analysis_name
):

    patients = load_patients()

    for patient in patients:

        if patient["patient_id"] == patient_id:

            patient[
                "analyses"
            ].append(
                {
                    "name":
                    analysis_name
                }
            )

    save_patients(patients)