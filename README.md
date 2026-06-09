# Calories-Burnt-Prediction

This project aims to predict the number of calories burned during physical activity using physiological and exercise-related parameters. The objective is to build regression models capable of estimating calorie expenditure accurately.

# Problem Statement

Accurately estimating calories burned can help individuals monitor fitness progress and optimize exercise routines. This project predicts calories burned based on biometric and activity-related features.

# Dataset

Features include:
- Age
- Gender
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature

Target:
- Calories Burned

**Source - Kaggle**

# Approach

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Train-Test Split
- Model Training and Evaluation

# Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

# Results
| Model                                      |     RMSE |   R² Score |
|:-------------------------------------------|---------:|-----------:|
| Linear Regression (Raw Target)             | 10.1149  |   0.974649 |
| Linear Regression (Log Transformed Target) | 23.4221  |   0.864068 |
| Random Forest                              |  6.05146 |   0.990926 |
| XGBoost Regressor                          |  5.9904  |   0.991108 |

XGBoost achieved the best overall performance on the dataset.

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Seaborn

# Key Learnings

- Regression Analysis
- Feature Engineering
- Model Evaluation
- Hyperparameter Tuning
- Feature Importance Analysis
