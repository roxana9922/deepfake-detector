"""
Grad-CAM explanation file for my COMP3000 deepfake detection project.

This file shows how the explanation stage works. In the full system, an image
would be passed through the trained model, and Grad-CAM would create a heatmap
showing which parts of the image had the most influence on the prediction.

This helps make the model easier to understand, instead of only showing a
real or fake result.
"""

import argparse
from pathlib import Path


def generate_gradcam(image_path):
    """
    Show the Grad-CAM workflow for one image.

    In the complete project, this function would:
    - load the image;
    - preprocess it in the same way as the model input;
    - run the trained EfficientNet-B0 model;
    - calculate the Grad-CAM heatmap;
    - overlay the heatmap on the image;
    - save or display the final explanation.
    """

    image_path = Path(image_path)

    print("Grad-CAM Explanation")
    print("--------------------")

    if not image_path.exists():
        print(f"Image not found: {image_path}")
        print("Please check the file path and try again.")
        return

    print(f"Input image: {image_path}")

    print("\nGrad-CAM process:")
    print("1. Load the image")
    print("2. Run the trained model")
    print("3. Find the image areas that influenced the prediction")
    print("4. Create a heatmap")
    print("5. Show the heatmap over the original image")

    print("\nExpected output:")
    print("Model prediction: Real or Fake")
    print("Grad-CAM output: Heatmap showing important image regions")

    print("\nImportant note:")
    print(
        "Grad-CAM helps explain what the model focused on, but it does not prove "
        "that the prediction is correct. It should be used to support human "
        "review and error analysis."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Grad-CAM explanation for one image."
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the image file to explain"
    )

    args = parser.parse_args()
    generate_gradcam(args.image)


if __name__ == "__main__":
    main()
