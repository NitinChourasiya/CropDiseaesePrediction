import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from backend.services.label_loader import load_labels
from pathlib import Path

from frontend.api_client import (
    predict,
    get_history,
    delete_prediction,
    delete_all_history
)
# http://localhost:8501


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
    image_path = Path("assets") / "Home.webp"
    img = Image.open(image_path)
    

    

    st.image(np.array(img))



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
    if st.button("Predict"):

        if test_image is None:
            st.warning("Please upload an image first.")
            st.stop()

        st.snow()

        st.write("### Prediction")

        try:

            result = predict(test_image)

        except RuntimeError as e:

            st.error(str(e))
            st.stop()

        st.success(
            f"Model is Predicting: {result['disease']}"
        )

        # st.write(
        #     st.metric("Confidence", f"{result['confidence']:.2%}")
        # )
        
elif app_mode == "Prediction History":

    st.header("Prediction History")

    rows = get_history()

    if len(rows) == 0:
        st.info("No predictions found.")

    else:

        history = []

        for row in rows:
            history.append({
                "ID": row["id"],
                "Time": row["timestamp"],
                "Model": row["model"],
                "Disease": row["disease"],
                "Image": row["image"],
                "Confidence": f"{row['confidence']:.2%}",
            })

        df = pd.DataFrame(history)

        # -------- Delete Selected --------

        col1, col2, col3= st.columns([4, 1,1])

        with col1:

            selected_id = st.selectbox(
                "Select Prediction to Delete",
                df["ID"].tolist(),
            )

        with col2:

            st.write("")

            if st.button("🗑 Delete Selected"):

                try:

                    delete_prediction(selected_id)

                    st.success("Prediction deleted successfully.")

                    st.rerun()

                except Exception as e:

                    st.error(str(e))

        with col3:

            st.write("")

            if st.button("🗑 Delete All"):

                try:

                    delete_all_history()

                    st.success("All history deleted successfully.")

                    st.rerun()

                except Exception as e:

                    st.error(str(e))
        # -------- Table --------

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )