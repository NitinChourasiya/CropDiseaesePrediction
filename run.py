import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd

from backend.explainability.gradcam import generate_gradcam
from backend.explainability.visualization import overlay_heatmap
from backend.services.model_loader import load_model
from backend.services.label_loader import load_labels
from backend.utils.image_loader import load_image

from database.db import initialize_database
from database.history import (
    save_prediction,
    get_prediction_history,
)
initialize_database()

def model_prediction(test_image):

    model = load_model()

    original_image, img_array = load_image(test_image)

    prediction = model.predict(img_array, verbose=0)

    result_index = np.argmax(prediction)

    return (
        model,
        original_image,
        img_array,
        prediction,
        result_index,
    )

# #Tensorflow model prediction
# def model_prediction(test_image):
#     model = load_model()
#     image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
#     input_arr=tf.keras.preprocessing.image.img_to_array(image)
#     input_arr=np.array([input_arr])
#     prediction=model.predict(input_arr)
#     result_index=np.argmax(prediction)
    
#     return result_index

#SideBar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select page",
    [
        "Home",
        "About",
        "Disease Recognition",
        "Prediction History",
    ]
)

#Home page
if(app_mode=="Home"):
    st.header("Plant Disease Recognition System")
    image_path="C:\\Users\\Lenovo\\Documents\\CropDiseaseDetectionDataset\\New Plant Diseases Dataset(Augmented)\\Home.webp"
    st.image(image_path)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍 
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

    #About
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
            #### About Dataset
            This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
            This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
            A new directory containing 33 test images is created later for prediction purpose.               
            #### Content
            1. train (70295 images)
            2. test (33 images)
            3. validation (17572 images)
    """)

#Prediction Page
elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):#If button is pressed then it will return true
        st.image(test_image,width=400)
    #Predict button
    # if(st.button("Predict")):
    #     st.snow()#st.balloons(), st.spinner()  can also be used
    #     st.write("Our Prediction")
    #     model, img_array, prediction, result_index = model_prediction(test_image)
    #     # result_index = model_prediction(test_image)
    #     #Reading Labels
    #     class_names = load_labels()

    #     st.success(f"Model is Predicting it's a {class_names[result_index]}")
    if st.button("Predict"):

        if test_image is None:
            st.warning("Please upload an image first.")
            st.stop()

        st.snow()

        st.write("### Prediction")

        model, original_image, img_array, prediction, result_index = model_prediction(test_image)

        class_names = load_labels()

        st.success(f"Model is Predicting: {class_names[result_index]}")
        #-----------------------
        #SQ-Lite
        confidence = float(prediction[0][result_index])

        image_name = test_image.name if test_image else None

        st.write("Saving prediction...")

        save_prediction(
            model_name="Custom CNN",
            disease_name=class_names[result_index],
            image_name=image_name,
            confidence=confidence,
        )
        st.write("prediction saved...")
        #-----------------------

        # -----------------------
        # Generate Grad-CAM
        # -----------------------
        # heatmap = generate_gradcam(
        #     model,
        #     img_array,
        #     result_index,
        #     "conv2d_7"
        # )   
        # print("Heatmap:", heatmap)

        # if heatmap is None:
        #     st.error("Grad-CAM returned None")
        #     st.stop()

        # print("Heatmap shape:", heatmap.shape)

        # # Convert uploaded image to numpy
        # original_image = np.array(original_image)
        
        # overlay = overlay_heatmap(
        #     original_image,
        #     heatmap
        # )

        # col1, col2 = st.columns(2)

        # with col1:
        #     st.subheader("Original Image")
        #     st.image(original_image, use_container_width=True)

        # with col2:
        #     st.subheader("Grad-CAM")
        #     st.image(overlay, use_container_width=True)

elif app_mode == "Prediction History":
        st.header("Prediction History")

        rows = get_prediction_history()
        # st.markdown("Number of rows:", len(rows))
        # st.write(rows)
        if len(rows) == 0:
            st.info("No predictions found.")
        else:

            history = []

            for row in rows:
                history.append({
                    "Time": row["timestamp"],
                    "Model": row["model_name"],
                    "Disease": row["disease_name"],
                    "Image": row["image_name"],
                    "Confidence": f"{row['confidence']:.2%}",
                })

            df = pd.DataFrame(history)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )