# Student Exam Performance Indicator

This is an **end-to-end machine learning project** that predicts a student's math score based on various input features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and reading/writing scores. The project includes a Flask-based web application and a Streamlit-based interactive interface for predictions.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview
The **Student Exam Performance Indicator** is designed to:
- Predict a student's math score based on input features.
- Provide an interactive interface for users to input data and view predictions.
- Demonstrate the use of machine learning pipelines for preprocessing and prediction.

---

## Features
- **Input Features**:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type
  - Test Preparation Course
  - Reading and Writing Scores
- **Prediction Output**:
  - Predicted Math Score
- **Web Interfaces**:
  - Flask-based web application.
  - Streamlit-based interactive interface.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pandas`, `numpy` - Data manipulation and analysis.
  - `scikit-learn` - Machine learning and preprocessing.
  - `catboost`, `xgboost` - Advanced machine learning models.
  - `Flask` - Web framework for the backend.
  - `Streamlit` - Interactive web application framework.
  - `matplotlib`, `seaborn` - Data visualization.
  - `dill` - Serialization of objects.
- **Tools**:
  - `requirements.txt` - Dependency management.

---

## Project Structure
```
ML_PRJ/
├── app.py                 # Main application file for Flask and Streamlit
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py  # Prediction pipeline and data preprocessing
│   │   └── train_pipeline.py    # Training pipeline (if applicable)
│   ├── exception.py       # Custom exception handling
│   ├── utils.py           # Utility functions (e.g., loading objects)
├── templates/
│   ├── home.html          # HTML template for Flask
│   └── index.html         # Landing page for Flask
├── static/
│   ├── css/
│   │   └── styles.css     # CSS for styling the Flask app
│   └── images/            # Images used in the project
├── artifacts/
│   ├── model.pkl          # Trained machine learning model
│   ├── preprocessor.pkl   # Preprocessing pipeline
│   └── data.csv           # Dataset used for training/testing
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── data/                  # Raw dataset (if applicable)
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ML_PRJ
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run the Flask Application
```bash
python app.py
```
- Open the application in your browser at `http://localhost:5000`.

### 2. Run the Streamlit Application
```bash
streamlit run app.py
```
- Open the application in your browser (Streamlit will provide a local URL, e.g., `http://localhost:8501`).

---

## Dataset
The dataset contains the following columns:
- `gender`: Gender of the student (e.g., male, female).
- `race_ethnicity`: Group of the student (e.g., group A, group B, etc.).
- `parental_level_of_education`: Parent's education level (e.g., bachelor's degree).
- `lunch`: Type of lunch (e.g., free/reduced, standard).
- `test_preparation_course`: Test preparation course status (e.g., none, completed).
- `reading_score`: Reading score (out of 100).
- `writing_score`: Writing score (out of 100).

---

## Model Training
The model was trained using the following steps:
1. **Data Preprocessing**:
   - Handled categorical features using `OneHotEncoder`.
   - Scaled numerical features using `StandardScaler`.
2. **Model Selection**:
   - Used `CatBoost` and `XGBoost` for regression.
3. **Evaluation**:
   - Evaluated the model using metrics like Mean Squared Error (MSE) and R².

---

## Future Enhancements
- Add support for additional features (e.g., science scores).
- Improve the user interface with more visualizations.
- Deploy the application to a cloud platform (e.g., AWS,Azure).

---


## Acknowledgments
- Libraries: `scikit-learn`, `catboost`, `xgboost`, `Flask`, `Streamlit`