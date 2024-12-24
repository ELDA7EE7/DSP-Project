# ECG Signal Classification Project

## Overview
This project aims to classify ECG signals as either **Normal** or **Left Bundle Branch Block (LBBB)** using machine learning models.  
The key steps involved include:
- Data preprocessing
- Feature extraction
- Model training and evaluation
- Deployment

---

## Introduction
This project leverages machine learning techniques to classify ECG signals as **Normal** or **LBBB**. It involves the following steps:
- Preprocessing ECG signals using **Butterworth bandpass filters**.
- Extracting features from the signals using **wavelet transforms**.
- Training and evaluating different machine learning models.
- Deploying the best model using a **GUI application**.

---

## Data Preprocessing
The data preprocessing step involves:
1. Removing noise from the ECG signals using a **Butterworth bandpass filter**.
2. Normalizing the signals to a standard range to ensure consistent feature extraction.

---

## Feature Extraction
Features are extracted from the preprocessed signals using **wavelet transforms**.  
Statistical features such as:
- Mean
- Standard deviation
- Skewness
- Kurtosis  
are calculated from the wavelet coefficients.

---

## Model Training and Evaluation
Various machine learning models are trained and evaluated on the extracted features, including:
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Random Forest**  

The best model is selected based on **accuracy** and other evaluation metrics.

---

## Deployment
The best-performing model (**KNN**) is deployed using a **GUI application**.  
This application allows users to:
- Input ECG signals
- Receive a classification result: **Normal** or **LBBB**

---

## Usage
To use the deployed model:
1. Run the `gui.py` file to start the GUI application.
2. Input your ECG signal into the application.
3. View the classification result (Normal or LBBB).

---

## Results
The project achieved impressive results:
- The best model (**KNN**) achieved an **accuracy of 98.75%** on the test set.
- Detailed evaluations and feature importances are documented in the project report.
