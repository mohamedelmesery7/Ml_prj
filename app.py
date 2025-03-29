import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Set the title of the app
st.title("Student Exam Performance Indicator")
st.subheader("Student Exam Performance Prediction")

# Create the form using Streamlit widgets
with st.form("prediction_form"):
    st.write("Please fill out the details below:")

    # Gender
    gender = st.selectbox("Gender", ["Select your Gender", "Male", "Female"])

    # Race or Ethnicity
    ethnicity = st.selectbox(
        "Race or Ethnicity",
        ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"],
    )

    # Parental Level of Education
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "Select Parent Education",
            "Associate's Degree",
            "Bachelor's Degree",
            "High School",
            "Master's Degree",
            "Some College",
            "Some High School",
        ],
    )

    # Lunch Type
    lunch = st.selectbox("Lunch Type", ["Select Lunch Type", "Free/Reduced", "Standard"])

    # Test Preparation Course
    test_preparation_course = st.selectbox(
        "Test Preparation Course", ["Select Test Course", "None", "Completed"]
    )

    # Reading Score
    reading_score = st.number_input(
        "Reading Score (out of 100)", min_value=0, max_value=100, step=1
    )

    # Writing Score
    writing_score = st.number_input(
        "Writing Score (out of 100)", min_value=0, max_value=100, step=1
    )

    # Submit button
    submitted = st.form_submit_button("Predict Your Math Score")

# Handle form submission
if submitted:
    # Validate inputs
    if (
        gender == "Select your Gender"
        or ethnicity == "Select Ethnicity"
        or parental_level_of_education == "Select Parent Education"
        or lunch == "Select Lunch Type"
        or test_preparation_course == "Select Test Course"
    ):
        st.error("Please fill out all the fields correctly.")
    else:
        # Normalize input categories to match the preprocessor's expectations
        data = CustomData(
            gender=gender.lower(),  # Convert to lowercase
            race_ethnicity=ethnicity,  # Convert to title case
            parental_level_of_education=parental_level_of_education.lower(),
            lunch=lunch.lower(),
            test_preparation_course=test_preparation_course.lower(),
            reading_score=reading_score,
            writing_score=writing_score,
        )

        # Convert data to DataFrame
        pred_df = data.get_data_as_data_frame()
        st.write("Input DataFrame:", pred_df)

        # Prediction pipeline
        predict_pipeline = PredictPipeline()
        st.write("Starting Prediction...")
        try:
            # Perform prediction
            results = predict_pipeline.predict(pred_df)
            st.success(f"The predicted Math Score is: {results[0]:.2f}")
        except Exception as e:
            # Handle errors during prediction
            st.error(f"An error occurred during prediction: {e}")