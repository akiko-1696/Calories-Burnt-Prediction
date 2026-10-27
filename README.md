# 🏋️‍♂️ Calories Burnt Prediction & Web Interface

This project is an end-to-end Machine Learning pipeline that predicts the number of calories burned during physical activity using physiological and exercise-related parameters. It features a highly accurate **XGBoost Regressor** deployed via an interactive **Streamlit web application**.

## 📌 Problem Statement
Accurately estimating calories burned can help individuals monitor fitness progress and optimize exercise routines. The objective of this project is to build a robust regression model capable of estimating calorie expenditure accurately based on biometric data, and to make those predictions accessible through a user-friendly web interface.

## 📊 Dataset
**Source:** Kaggle

**Raw Features:**
- Gender
- Age
- Height (cm)
- Weight (kg)
- Exercise Duration (minutes)
- Heart Rate (bpm)
- Body Temperature (°C)

**Target Variable:**
- Calories Burned

## 🚀 Approach & Feature Engineering
To maximize model accuracy, raw biometric data was engineered into complex features before training:
1. **Data Cleaning & EDA:** Visualized distributions and handled missing values.
2. **Feature Engineering:** 
   - `BMI` = Weight / (Height in m)²
   - `Total_Exertion` = Duration × Heart Rate
   - `Temp_Spike` = Body Temperature - 37.0°C
3. **Train-Test Split & Scaling**
4. **Model Training & Hyperparameter Tuning**
5. **Web Deployment:** Built a frontend using Streamlit that automatically applies the feature engineering pipeline to user inputs in real-time before passing them to the saved model.

## 🏆 Model Performance
Multiple regression models were evaluated. The **XGBoost Regressor** achieved the best overall performance and was selected as the production model for the web application.

| Model | RMSE | R² Score |
|-------|------|----------|
| Linear Regression (Raw Target) | 10.1149 | 0.9746 |
| Linear Regression (Log Transformed) | 23.4221 | 0.8640 |
| Random Forest | 6.0514 | 0.9909 |
| **XGBoost Regressor** | **5.9904** | **0.9911** |

## 💻 Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost, Matplotlib, Seaborn
- **Deployment:** Streamlit, Pickle

## ⚙️ How to Run the Web App Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/Calories-Burnt-Prediction.git](https://github.com/your-username/Calories-Burnt-Prediction.git)
   cd Calories-Burnt-Prediction
