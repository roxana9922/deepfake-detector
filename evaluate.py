"""
Evaluation file for my COMP3000 deepfake detection project.

This file shows the main results from the final model. I used accuracy,
precision, recall, F1-score, ROC-AUC and a confusion matrix to understand how
well the model performed.

The results show that the model can detect some useful patterns, but it still
makes too many mistakes to be used on its own in a cybersecurity setting.
"""


def main():
    print("Deepfake Detection Results")
    print("--------------------------")

    print("Accuracy: 71.37%")
    print("Precision: 71.11%")
    print("Recall: 72.00%")
    print("F1-score: 71.55%")
    print("ROC-AUC: 0.7888")

    print("\nConfusion Matrix:")
    print("True Positives: 283")
    print("False Negatives: 117")
    print("False Positives: 112")
    print("True Negatives: 288")

    print("\nWhat the results mean:")
    print(
        "The model performed at a moderate level. It was fairly balanced, "
        "but it was not accurate enough to be trusted as a final decision-maker."
    )
    print(
        "The false negatives are the main concern because these are fake images "
        "that the model predicted as real."
    )
    print(
        "False positives also matter because they are real images that were "
        "wrongly flagged as fake."
    )
    print(
        "For this reason, the system is better used as a support tool for a "
        "human analyst, not as a fully automatic detector."
    )


if __name__ == "__main__":
    main()
