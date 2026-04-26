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

- Image-based deepfake detection
- Binary classification: real vs fake
- Facial image preprocessing
- EfficientNet-B0 CNN architecture
- TensorFlow/Keras implementation
- Grad-CAM visual explainability
- Evaluation using multiple performance metrics
- Confusion matrix and ROC-AUC analysis
- Lightweight demonstration interface
- Cybersecurity-focused discussion of reliability and risk

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

## Dataset

The project used publicly available deepfake detection datasets, mainly:

- **FaceForensics++**
- **Celeb-DF v2**

The dataset was balanced between real and fake facial images. Images were processed using face detection, resizing, normalisation and data augmentation before training.

The augmentation process included:

- compression simulation;
- Gaussian blur;
- image noise;
- colour variation;
- random cropping and scaling.

These steps were included to reflect some of the conditions that occur in real-world media, such as social media compression, reduced image quality, lighting changes and resizing.

The full datasets are not included in this repository due to size and licensing restrictions.

---

## Model

The final model uses **EfficientNet-B0** with ImageNet-pretrained weights as the CNN-based feature extractor.

EfficientNet-B0 was selected because it provided a practical balance between performance and computational cost. This was important because the project was completed under undergraduate hardware and time constraints.

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

The model achieved moderate but balanced performance.

| Metric | Result |
|---|---:|
| Accuracy | 71.37% |
| Precision | 71.11% |
| Recall | 72.00% |
| F1-score | 71.55% |
| ROC-AUC | 0.7888 |

### Confusion Matrix Summary

| Classification Result | Count |
|---|---:|
| True Positives | 283 |
| False Negatives | 117 |
| False Positives | 112 |
| True Negatives | 288 |

The results show that the model learned useful patterns for separating real and fake images. However, the overall error rate remains too high for fully automated cybersecurity use.

The false negatives are particularly important because they represent fake images that were classified as real. In a cybersecurity setting, this could allow manipulated media to be used for impersonation, fraud or misinformation. False positives are also relevant because they could cause genuine images to be wrongly flagged, increasing analyst workload and reducing trust in the system.

For this reason, the prototype is best understood as a **decision-support tool** for human analysts rather than a fully autonomous detector.

---

## Grad-CAM Explainability

Grad-CAM was integrated to make the model’s predictions easier to interpret. It produces a heatmap showing which regions of the image contributed most strongly to the model’s decision.

This was used to check whether the model focused on meaningful facial areas or on less reliable features such as:

- background artefacts;
- compression patterns;
- lighting differences;
- low-resolution areas;
- non-facial regions.

The Grad-CAM analysis showed mixed behaviour. Some correct predictions focused on plausible facial regions, while some failure cases suggested that the model may have relied on background details or compression artefacts. This indicates possible shortcut learning, where the model learns patterns that work in the dataset but may not generalise well to unseen real-world images.

Grad-CAM is therefore treated as an interpretation and debugging tool, not as proof that the model prediction is correct.

---

## Demonstration Artefact

A lightweight demonstration interface was developed to show how the system could be used by a user or analyst. The interface allows an image to be uploaded and is designed to display:

- the uploaded image;
- the real/fake prediction;
- the confidence score;
- the Grad-CAM heatmap;
- a warning that the result should be reviewed by a human.

The demonstrator is a research prototype and is not intended for production or high-stakes decision-making.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/roxana9922/deepfake-detector.git
cd deepfake-detector
