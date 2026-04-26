
"""
Single-image prediction script for my COMP3000 deepfake detection project.

This file shows the prediction workflow for one uploaded image. In the full
system, the image would be loaded, preprocessed in the same way as the training
data, passed through the trained EfficientNet-B0 model, and returned with a
real/fake prediction and confidence score.

The script is written to make the workflow clear and easy to follow.
"""

import argparse
from pathlib import Path


def predict_image(image_path):
    """
    Show the prediction workflow for one image.

    In the complete project, this function would:
    - load the image;
    - detect and crop the face;
    - resize the image to 224 x 224;
    - normalise the image;
    - run the trained EfficientNet-B0 model;
    - return the predicted class and confidence score.
    """

    image_path = Path(image_path)

    print("Deepfake Detection Prediction")
    print("-----------------------------")

    if not image_path.exists():
        print(f"Image not found: {image_path}")
        print("Please check the file path and try again.")
        return

    print(f"Input image: {image_path}")

    print("\nPrediction process:")
    print("1. Load the image")
    print("2. Detect and crop the face")
    print("3. Resize and normalise the image")
    print("4. Run the trained model")
    print("5. Return the predicted class and confidence score")

    print("\nExpected output:")
    print("Predicted class: Real or Fake")
    print("Confidence score: Displayed with the prediction")

    print("\nImportant note:")
    print(
        "This output should support human review. It should not be used as a "
        "final automated cybersecurity decision."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Run a deepfake prediction on one image."
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the image file to analyse"
    )

    args = parser.parse_args()
    predict_image(args.image)


if __name__ == "__main__":
    main()
