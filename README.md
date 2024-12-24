					        ECG Signal Classification Project
Overview
	
        This project aims to classify ECG signals as either Normal or Left Bundle Branch Block (LBBB) using machine learning models.
        The key steps involved include data preprocessing, feature extraction, model training, evaluation, and deployment.

Introduction
	
         This project uses machine learning techniques to classify ECG signals as Normal or LBBB. It involves the following steps:
			- Preprocessing ECG signals using Butterworth bandpass filters.
			- Extracting features from the signals using wavelet transforms.
			- Training and evaluating different machine learning models.
			- Deploying the best model using a GUI application.

Data Preprocessing
	
          The data preprocessing step involves removing noise from the ECG signals using a Butterworth bandpass filter.
          The signals are then normalized to a standard range for consistent feature extraction.

Feature Extraction
	
         Features are extracted from the preprocessed signals using wavelet transforms. 
         Statistical features such as mean, standard deviation, skewness, and kurtosis are then calculated from the wavelet coefficients.

Model Training and Evaluation
	
         Different machine learning models such as K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Random Forest 
         are trained and evaluated on the extracted features. The best model is selected based on accuracy and other evaluation metrics.

Deployment
	
         The best-performing model (KNN) is deployed using a GUI application. 
         The application allows users to input ECG signals and get a classification result (Normal or LBBB).

Usage
	
         To use the deployment model, you need to run the gui.py file. This will start the GUI application where you can read your ECG signal,
         and it will label it as either Normal or LBBB. Use the application to input your ECG signal and obtain the classification result.

Results
          
          The results of the model evaluations and feature importances are documented in the project. The best model(KNN) achieved an accuracy of 98.75% on the test set.

Acknowledgments
          
          Special thanks to all the contributors and the open-source community for providing the necessary tools and datasets to make this project possible.
