import json
import streamlit as st


@st.cache_data
def load_labels():
    """
    Load disease class labels from a JSON file.
    """

    with open("backend/data/labels.json", "r") as file:
        return json.load(file)