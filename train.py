"""
Training setup for my COMP3000 deepfake detection project.

This file shows the main settings used to train the model. The project used
EfficientNet-B0 to classify face images as real or fake.

Before training, the images were prepared by detecting the face, resizing the
image, normalising it, and applying data augmentation.
"""

def main():
    print("Deepfake Detection Training Setup")
    print("---------------------------------")

    print("Model: EfficientNet-B0")
    print("Input size: 224 x 224")
    print("Task: Real/Fake image classification")
    print("Optimiser: Adam")
    print("Learning rate: 0.0001")
    print("Batch size: 16")
    print("Loss function: Binary cross-entropy")
    print("Early stopping: Enabled")

    print("\nNotes:")
    print(
        "EfficientNet-B0 was used because it is a good balance between "
        "accuracy and training time."
    )
    print(
        "Data augmentation was added to help the model handle changes such as "
        "blur, noise, compression and lighting."
    )
    print(
        "The model reached moderate performance, so the project also focused "
        "on understanding its limits rather than only improving accuracy."
    )


if __name__ == "__main__":
    main()
