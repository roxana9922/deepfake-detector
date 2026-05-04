# Explainable Deepfake Detection for Cybersecurity

## Project Overview

This repository contains the implementation for my COMP3000 Final Year Computing Project at the University of Plymouth.

The project investigates whether an explainable AI-based deepfake detection system can support cybersecurity decision-making. The system uses a CNN-based image classification pipeline to classify facial images as **real** or **fake**, and integrates **Grad-CAM** to provide visual explanations of model predictions.

The focus of the project is not only classification accuracy, but also robustness, dataset bias, explainability, generalisation risk, and the limitations of deploying deepfake detectors in realistic cybersecurity scenarios.

## Project Title

**Explainable Deepfake Detection for Cybersecurity: Evaluating Robustness, Explainability and Generalisation Risk in AI Media Forensics**

## Student

**Elena Iordache**  
BSc (Hons) Computer Science – Cyber Security  
University of Plymouth

## Supervisor

**Dr Bogdan Ghita**

---

## Key Features

- Image-based deepfake detection
- Binary classification: real vs fake
- Facial image preprocessing
- EfficientNet-B0 CNN architecture
- TensorFlow/Keras implementation
- Grad-CAM visual explainability
- Evaluation using accuracy, precision, recall, F1-score and ROC-AUC
- Confusion matrix and ROC curve analysis
- Held-out external evaluation with leakage-control checks
- Lightweight demonstration interface
- Cybersecurity-focused interpretation of reliability, false positives and false negatives

---

## Technologies Used

- Python
- TensorFlow / Keras
- EfficientNet-B0
- NumPy
- OpenCV
- Matplotlib
- Scikit-learn
- Grad-CAM
- Jupyter Notebook / Python scripts

---

## Dataset Information

The project uses publicly available deepfake detection datasets, including:

- FaceForensics++
- Celeb-DF v2

The experimental dataset was balanced between real and fake facial images. Images were processed using face detection, resizing, normalisation and data augmentation before training.

Data augmentation included:

- compression simulation
- Gaussian blur
- image noise
- colour variation
- random cropping and scaling

These steps were included to reflect conditions that occur in real-world media, such as social media compression, reduced image quality, lighting changes and resizing.

The full datasets are **not included** in this repository due to size and licensing restrictions.

---

## Model

The final model uses **EfficientNet-B0** with ImageNet-pretrained weights as the CNN-based feature extractor.

EfficientNet-B0 was selected because it provides a practical balance between classification performance and computational cost. This was important because the project was completed under undergraduate hardware and time constraints.
The screenshots folder contains evidence of the Streamlit demonstration interface running successfully.

| Parameter | Value |
|---|---|
| Model | EfficientNet-B0 |
| Input size | 224 × 224 |
| Classification task | Binary classification |
| Optimiser | Adam |
| Learning rate | 0.0001 |
| Batch size | 16 |
| Loss function | Binary cross-entropy |
| Early stopping | Enabled |

---

## Results

The model achieved moderate but balanced performance on the controlled evaluation set.

| Metric | Result |
|---|---:|
| Accuracy | 71.37% |
| Precision | 71.11% |
| Recall | 72.00% |
| F1-score | 71.55% |
| ROC-AUC | 0.7888 |

### Confusion Matrix Summary

| Classification result | Count |
|---|---:|
| True positives | 283 |
| False negatives | 117 |
| False positives | 112 |
| True negatives | 288 |

The results show that the model learned useful patterns for separating real and fake images. However, the overall error rate remains too high for fully automated cybersecurity use.

False negatives are particularly important because they represent fake images that were classified as real. In a cybersecurity setting, this could allow manipulated media to support impersonation, fraud or misinformation. False positives are also relevant because they could cause genuine images to be wrongly flagged, increasing analyst workload and reducing trust in the system.

For this reason, the prototype is best understood as a **decision-support tool** for human analysts rather than a fully autonomous detector.

---

## Held-Out External Evaluation

An additional held-out external evaluation was carried out to assess generalisation risk more critically.

Before evaluation, hash-based duplicate checking was used to identify and remove exact overlap between the training data and the held-out evaluation set. After leakage-control checks, the final held-out external evaluation set contained 616 images.

| Metric | Result |
|---|---:|
| Accuracy | 69.97% |
| Precision | 71.52% |
| Recall | 68.57% |
| F1-score | 70.02% |
| ROC-AUC | 0.7491 |

This result suggests that the model retained some transferable detection ability, but performance remained limited. It should therefore not be interpreted as a production-ready or legally reliable forensic tool.

---

## Grad-CAM Explainability

Grad-CAM was integrated to make the model’s predictions easier to interpret. It produces a heatmap showing which regions of the image contributed most strongly to the model’s decision.

Grad-CAM was used to check whether the model focused on meaningful facial areas or on less reliable features such as:

- background artefacts
- compression patterns
- lighting differences
- low-resolution regions
- non-facial areas

The Grad-CAM analysis showed mixed behaviour. Some correct predictions focused on plausible facial regions, while some failure cases suggested that the model may have relied on background details or compression artefacts. This indicates possible shortcut learning, where the model learns patterns that work in the dataset but may not generalise well to unseen real-world images.

Grad-CAM is therefore treated as an **interpretation and debugging tool**, not as proof that the model prediction is correct.

---

## Demonstration Artefact

A lightweight demonstration interface was developed to show how the system could be used by a user or analyst. The interface allows an image to be uploaded and is designed to display:

- the uploaded image
- the real/fake prediction
- the confidence score
- the Grad-CAM heatmap
- a warning that the result should be reviewed by a human

The demonstrator is a research prototype and is not intended for production or high-stakes decision-making.

---

## Repository Structure

```text
deepfake-detector/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── data_preparation.ipynb
│   ├── model_training.ipynb
│   ├── evaluation.ipynb
│   └── gradcam_explainability.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── gradcam.py
│   └── app.py
│
├── models/
│   └── README.md
│
├── screenshots/
│   ├── training_evidence.png
│   ├── evaluation_metrics.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── gradcam_example.png
│
└── docs/
    └── project_report_summary.pdf
