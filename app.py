"""
Small Streamlit demo for my COMP3000 deepfake detection project.

The app lets a user upload a face image and shows how the final system would
present a real/fake prediction together with a Grad-CAM explanation.

This is not meant to be a production security tool. It is a prototype built to
demonstrate the workflow and to support the evaluation in my final report.
"""

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Deepfake Detection Demo",
    page_icon="🛡️",
    layout="centered"
)


st.title("Explainable Deepfake Detection")

st.write(
    """
    This demo is part of my final year project on deepfake detection for
    cybersecurity. The idea is to test whether a CNN-based model can help
    identify fake facial images, while also giving the user some explanation of
    why the model made its prediction.
    """
)

st.write(
    """
    The project is not only about getting a prediction. It also looks at how much
    trust should be placed in that prediction, especially because mistakes in a
    cybersecurity setting could lead to false accusations, missed deepfakes, or
    extra work for analysts.
    """
)

st.warning(
    """
    This prototype should be used for demonstration and evaluation only. The
    output should always be checked by a human and should not be treated as a
    final decision.
    """
)

uploaded_file = st.file_uploader(
    "Upload a face image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")
    st.image(image, caption="Image selected for analysis", use_container_width=True)

    st.subheader("Prediction")

    st.info(
        """
        In the full system, this section would show the model's prediction
        using the trained EfficientNet-B0 detector.
        """
    )

    st.markdown(
        """
        The output would include:

        - whether the image is predicted as real or fake;
        - the confidence score;
        - a short warning about human review.
        """
    )

    st.subheader("Grad-CAM Explanation")

    st.info(
        """
        This section would show the Grad-CAM heatmap for the uploaded image.
        The heatmap helps show which parts of the image had the most influence
        on the model's prediction.
        """
    )

    st.write(
        """
        This is useful because a model can sometimes focus on the wrong things,
        such as compression artefacts, lighting, or background areas. In this
        project, Grad-CAM is used to support interpretation, not to prove that
        the prediction is correct.
        """
    )

else:
    st.write("Upload an image to start.")
