import os
import streamlit as st
import tensorflow as tf


@st.cache_resource
def load_model():
    # """
    # Load the CNN model once and cache it.
    # """
    model_path = os.path.join("models", "model_epoch_05.keras")

    # Temporary fallback while we are refactoring
    if not os.path.exists(model_path):
        model_path = "model_epoch_05.h5"

    return tf.keras.models.load_model(model_path)