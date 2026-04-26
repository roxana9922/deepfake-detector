# Explainable Deepfake Detection for Cybersecurity

## Project Overview

This repository contains the implementation for my COMP3000 Final Year Computing Project at the University of Plymouth.

The project investigates whether an explainable AI-based deepfake detection system can support cybersecurity decision-making. The system uses a CNN-based image classification pipeline to classify facial images as **real** or **fake**, and integrates **Grad-CAM** to provide visual explanations of model predictions.

The project focuses not only on model accuracy, but also on robustness, dataset bias, explainability, and the limitations of deploying deepfake detectors in realistic cybersecurity scenarios.

## Project Title

**Explainable Deepfake Detection for Cybersecurity: Evaluating Robustness and Cross-Dataset Generalisation**

## Student

**Elena Iordache**  
BSc (Hons) Computer Science – Cyber Security  
University of Plymouth  

## Supervisor

**Dr Bogdan Ghita**

---

## Key Features

- Image-based deepfake classification
- Real/fake binary prediction
- Facial region preprocessing
- CNN-based model using EfficientNet-B0
- TensorFlow/Keras implementation
- Grad-CAM visual explanation
- Evaluation using accuracy, precision, recall, F1-score and ROC-AUC
- Confusion matrix and error analysis
- Cybersecurity-focused interpretation of false positives and false negatives

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

The final dataset was balanced between real and fake facial images. The images were preprocessed through face detection, resizing, normalisation and augmentation before training.

Data augmentation included:

- compression simulation
- Gaussian blur
- image noise
- colour variation
- random cropping and scaling

Due to dataset size and licensing restrictions, the full datasets are not included in this repository. Instructions are provided for preparing the dataset locally.

---

## Model Details

The final model uses **EfficientNet-B0** as a CNN-based feature extractor with ImageNet-pretrained weights.

Training configuration:

| Parameter | Value |
|---|---|
| Model | EfficientNet-B0 |
| Input size | 224 × 224 |
| Task | Binary classification |
| Optimiser | Adam |
| Learning rate | 0.0001 |
| Batch size | 16 |
| Loss function | Binary cross-entropy |
| Early stopping | Enabled |

---

## Results

The model achieved the following performance on the test set:

| Metric | Result |
|---|---|
| Accuracy | 71.37% |
| Precision | 71.11% |
| Recall | 72.00% |
| F1-score | 71.55% |
| ROC-AUC | 0.7888 |

Confusion matrix summary:

| Result | Count |
|---|---:|
| True Positives | 283 |
| False Negatives | 117 |
| False Positives | 112 |
| True Negatives | 288 |

The results show moderate and balanced classification performance. However, the error rate is too high for fully automated cybersecurity deployment. The system is therefore best interpreted as a **decision-support prototype**, not a final authority.

---

## Grad-CAM Explainability

Grad-CAM was integrated to visualise which regions of the image influenced the model prediction.

This was used to assess whether the model focused on meaningful facial regions or unreliable features such as:

- background artefacts
- compression patterns
- low-resolution areas
- lighting effects

Grad-CAM helped identify possible shortcut learning and supported the project’s critical evaluation of model reliability.

---

## How to Install

Clone the repository:

```bash
git clone https://github.com/roxana9922/deepfake-detector.git
cd deepfake-detector
