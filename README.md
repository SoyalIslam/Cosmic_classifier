🚀 Cosmic Classifier Challenge Report

🌌 Theme

The Galactic Classification Challenge (GCC) is a futuristic machine learning competition where participants must decode Dr. Klaus Reinhardt’s final transmission. The objective is to classify planets based on their survival potential and resource availability using machine learning techniques.

🛰️ Introduction

In the year 2547, Dr. Klaus Reinhardt, a renowned scientist and space explorer, made an extraordinary discovery while exploring a distant galaxy. He developed a system to classify planets based on their habitability and resource potential. However, before he could fully transmit his findings to Earth, his ship was caught in a black hole’s gravitational field. His final transmission, containing valuable planetary classification data, was corrupted due to gravitational interference, introducing missing values and noise.

🌍 Humanity’s survival depends on correctly classifying these planets using the available data.

🔍 Problem Statement

Participants are given a dataset containing planetary attributes and must develop a classification model to assign each planet to one of ten planetary classes. The dataset is partially corrupted, requiring participants to handle missing values and noise efficiently.

📊 Dataset Details

The dataset consists of 10 input features and 10 output classes, with data irregularities such as missing values marked by large negative numbers.

🌎 Input Features (10 planetary attributes)

Atmospheric Density (kg/m³) – Thickness of the atmosphere.

Surface Temperature (Kelvin) – Average temperature of the planet’s surface.

Gravity (m/s²) – Surface gravity of the planet.

Water Content (%) – Percentage of surface covered by water.

Mineral Abundance (0-1) – Availability of valuable minerals.

Orbital Period (Earth days) – Time taken to orbit its star.

Proximity to Star (AU) – Distance from its parent star.

Magnetic Field Strength (Tesla) – Strength of the planet’s magnetic field.

Radiation Levels (Sieverts/year) – Average surface radiation exposure.

Atmospheric Composition Index (0-1) – Suitability of the atmosphere for human life.

🪐 Output Classes (10 planetary types)

🌍 Bewohnbar

🏗 Terraformierbar

⛏ Rohstoffreich

🔬 Wissenschaftlich

☁ Gasriese

🏜 Wüstenplanet

❄ Eiswelt

☠ Toxischetmosäre

⚡ Hohestrahlung

💀 Toterahswelt

🎯 Project Goals

The primary objective is to develop a robust machine learning classification model to accurately categorize planets based on their features. Given the noisy nature of the dataset, preprocessing steps such as handling missing values, feature scaling, and dimensionality reduction are necessary.

🛠 Methodology

1️⃣ Data Preprocessing

Handling Missing Values: Identified missing values (-999 or other outliers) and replaced them using mean/median imputation.

Feature Scaling: Normalized numerical features to ensure uniformity.

Outlier Detection: Applied statistical techniques to detect and remove anomalies.

Feature Engineering: Created additional relevant features where necessary.

2️⃣ Model Selection

We experimented with multiple machine learning models:

🤖 Logistic Regression

🌲 Random Forest Classifier

🔥 Gradient Boosting (XGBoost, LightGBM, CatBoost)

📈 Support Vector Machines (SVM)

🧠 Neural Networks (MLPClassifier from sklearn)

3️⃣ Model Training and Evaluation

Split the data into training (80%) and validation (20%) sets.

Tuned hyperparameters using GridSearchCV and RandomizedSearchCV.

Evaluated models using accuracy, precision, recall, and F1-score.

4️⃣ Final Model Selection

After comparing multiple models, we selected XGBoost, which achieved the highest accuracy on the validation set.

📈 Results and Analysis

🏆 Best Model Accuracy: XGBoost with 91.5% validation accuracy

📊 Confusion Matrix Analysis: Showed some misclassifications in similar planet categories.

📌 Feature Importance: Gravity, Atmospheric Density, and Water Content were the most critical features.

🚀 Model Explanation: XGBoost

XGBoost (Extreme Gradient Boosting) is a powerful ensemble learning algorithm that builds multiple decision trees iteratively, minimizing errors at each step.

✅ Key Strengths of XGBoost:

🔄 Boosting Mechanism – Improves weak learners sequentially, reducing bias.

❓ Handling Missing Values – Automatically determines optimal splits even with missing data.

📊 Feature Importance Analysis – Identifies which features have the most impact on classification.

🛑 Regularization (L1 & L2) – Prevents overfitting by penalizing complex models.

⚡ Parallel Processing – Enhances computational efficiency, making it suitable for large datasets.

🛠 Hyperparameter Tuning for XGBoost:

Parameter

Value

n_estimators

200

max_depth

6

learning_rate

0.1

subsample

0.8

colsample_bytree

0.8

📌 Conclusion

The Galactic Classification Challenge successfully demonstrated the power of machine learning in planetary classification. XGBoost emerged as the best-performing model with an impressive 91.5% validation accuracy. Future improvements could include deep learning techniques and advanced feature engineering.

🌟 This project takes humanity one step closer to interstellar exploration! 🚀

👥 Team Details

🧑‍🚀 Tapas Pandey: https://github.com/Tapas-Pandey

🛰 Kartike Veram: https://github.com/kartikeVr

📊 Soyal Islam: https://github.com/SoyalIslam

💻 Dev Saini: https://github.com/devsaini889

🎨 Khushi Singh: https://github.com/khushisingh14

📷 Visuals









