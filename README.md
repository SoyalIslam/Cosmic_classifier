# 🚀 Cosmic Classifier Challenge Report

---

## 🌌 Theme
### **Galactic Classification Challenge (GCC)**
The **Galactic Classification Challenge** is a futuristic machine learning competition where participants must decode **Dr. Klaus Reinhardt’s** final transmission. The objective is to classify planets based on their **survival potential** and **resource availability** using machine learning techniques.

---

## 🛰️ Introduction
In the year **2547**, **Dr. Klaus Reinhardt**, a renowned scientist and space explorer, developed a **planetary classification system**. Before he could transmit his full findings to Earth, his ship was caught in a black hole’s gravitational field, corrupting his final transmission. 

🔍 **Mission:** Humanity’s survival depends on correctly classifying these planets using the available **noisy dataset**.

---

## 🔍 Problem Statement
Participants are given a **dataset containing planetary attributes** and must develop a **classification model** to assign each planet to one of **ten planetary classes**. The dataset is **partially corrupted**, requiring **handling of missing values and noise** efficiently.

---

## 📊 Dataset Details
The dataset consists of **10 input features** and **10 output classes**, with missing values marked by **large negative numbers**.

### 🌎 **Input Features**
| Feature | Description |
|---------|-------------|
| **Atmospheric Density (kg/m³)** | Thickness of the atmosphere |
| **Surface Temperature (Kelvin)** | Average temperature of the planet’s surface |
| **Gravity (m/s²)** | Surface gravity of the planet |
| **Water Content (%)** | Percentage of surface covered by water |
| **Mineral Abundance (0-1)** | Availability of valuable minerals |
| **Orbital Period (Earth days)** | Time taken to orbit its star |
| **Proximity to Star (AU)** | Distance from its parent star |
| **Magnetic Field Strength (Tesla)** | Strength of the planet’s magnetic field |
| **Radiation Levels (Sieverts/year)** | Average surface radiation exposure |
| **Atmospheric Composition Index (0-1)** | Suitability of the atmosphere for human life |

### 🪐 **Output Classes**
- 🌍 **Bewohnbar** (Habitable)
- 🏗 **Terraformierbar** (Terraformable)
- ⛏ **Rohstoffreich** (Resource-rich)
- 🔬 **Wissenschaftlich** (Scientific value)
- ☁ **Gasriese** (Gas giant)
- 🏜 **Wüstenplanet** (Desert planet)
- ❄ **Eiswelt** (Ice world)
- ☠ **Toxischetmosäre** (Toxic atmosphere)
- ⚡ **Hohestrahlung** (High radiation)
- 💀 **Toterahswelt** (Dead planet)

---

## 🎯 Project Goals
The primary goal is to develop a **robust machine learning classification model** that accurately categorizes planets. The dataset is noisy, requiring **advanced preprocessing, feature engineering, and hyperparameter tuning**.

---

## 🛠 Methodology
### 1️⃣ **Data Preprocessing**
- **Handling Missing Values**: Replaced `-999` values using **mean/median imputation**.
- **Feature Scaling**: Applied **StandardScaler** for uniformity.
- **Outlier Detection**: Used **IQR and Z-score methods** to remove anomalies.
- **Feature Engineering**: Created additional features like **habitability score**.

### 2️⃣ **Model Selection**
We experimented with multiple ML models:
- 🤖 **Logistic Regression**
- 🌲 **Random Forest Classifier**
- 🔥 **Gradient Boosting (XGBoost, LightGBM, CatBoost)**
- 📈 **Support Vector Machines (SVM)**
- 🧠 **Neural Networks (MLPClassifier from sklearn)**

### 3️⃣ **Model Training and Evaluation**
- **Train-Test Split**: **80% training, 20% validation**.
- **Hyperparameter Tuning**: Used **GridSearchCV & RandomizedSearchCV**.
- **Evaluation Metrics**: Measured **accuracy, precision, recall, and F1-score**.

### 4️⃣ **Final Model Selection**
🚀 **Best Model**: **XGBoost** achieved the highest **99.55% model performance**.

---

## 📈 Results and Analysis
### 🏆 **Best Model: XGBoost**
- **Model Performance**: **99.55%**
- **Feature Importance**:
  - **Gravity** 🪨, **Atmospheric Density** ☁, and **Water Content** 🌊 were key factors.
- **Confusion Matrix**: Minor misclassifications between **Terraformable & Habitable planets**.

### 🔧 **Hyperparameter Tuning for XGBoost**
```python
from xgboost import XGBClassifier
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8
)
model.fit(X_train, y_train)
```

---

## 📌 Conclusion
The **Galactic Classification Challenge** demonstrated the power of machine learning in planetary classification. 
🚀 **XGBoost emerged as the best-performing model with 99.55% model performance**.
### 🔮 **Future Scope**
- 🔭 **Deep Learning**: Use **CNNs & RNNs** for classification.
- 🌍 **Geospatial Analysis**: Integrate planetary mapping.
- 📡 **Reinforcement Learning**: Explore adaptive learning models.

---

## 👥 Team Details
🧑‍🚀 **Tapas Pandey**: [GitHub](https://github.com/Tapas-Pandey)  
🛰 **Kartike Veram**: [GitHub](https://github.com/kartikeVr)  
📊 **Soyal Islam**: [GitHub](https://github.com/SoyalIslam)  
💻 **Dev Saini**: [GitHub](https://github.com/devsaini889)  
🎨 **Khushi Singh**: [GitHub](https://github.com/khushisingh14)  

| Role | Name |
|------|------|
| **🧑‍🚀 Team Leader** | Tapas Pandey |
| **🛰 AI/ML Engineer** | Kartike Veram |
| **📊 Data Scientist** | Soyal Islam |
| **💻 Software Developer** | Dev Saini |
| **🎨 UI/UX Designer** | Khushi Singh |

---
## ⚙️ Installation

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/SoyalIslam/Cosmic_classifier.git
cd Cosmic_classifier
```
2️⃣ Create a Virtual Environment (Optional but recommended)
```sh
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```
3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
4️⃣ Run the Streamlit App
```sh
streamlit run app.py
```
## 📷 Visuals
![Home](https://lh3.googleusercontent.com/fife/ALs6j_EcCIoMLcgkivI_TfdeRHgOdhNPeArts3K8p7iMY7kW7QHPVFDzj1zXYaM0jMMX6JRjPUG7c_p9d_8xb7-8a8dYz7zxuZwseNQLJT9zl-rojQ4iWstAvICIUD3aQj12MsdM31kBmv7fCROWTpe9It78BHYEcWjHSAmnieD60VCms1G9YlwLtaZPlODXrCIYf96X2ZrbWuJCYwCTMjiaSYtW0EuLhzp2Wo_dcnVVQE9MeTR7XK_R_a8KYVdVW7AibOQNVHS2Lxvcao_ESVFZqnh78gcLX5bjhmvQJBMN5X1L_jYDDSrfqMGc-P86wSUn7-wRaNnTiSjFeK-sQDbclBzGaRIpLc0SIdjHCAhbXpdr7qHineiltqyaQoghbNHrjGJEJERO6a_jmiFD1QdGEPzXn84pJqBtqal5S7XE35Dukb34Fwf3hER2FA2G__hupb8f2wYyGWAMP9kl1OMn06LtFD6waKainsvO-Tdz1cef9NgsSyH-UiRDzni7-oT0VuX1LHFmQQLdbkjCOkeni9j1vBtgUt8J2MICdbphmFVjL4i2gD7BtR0-eTsTYDvGJqxPnxo00QOOMMsLD52vyrJYLR_fSreDb5q66yIKVJno-H5uYc65yqQmKrBBaNNoDMX7i3bt-eNBuM9kYZkVQe718_-1Y0M11fDuyXv2KjXR6bMhxmPJ5_ze7OSLvJNUtmki0DtfafEo4tr9jsNH1au6wb40Zi18Yf8XA26P7cZQqb1Y9UXungHBM-C2ivr-g7bw2z2QCAgftcCGG6tDNyFEPsSyhBTtzIGqkbATnwawLBlDpuRvOya9VCAxQAqiITyQKuX1BzXDn9hFDQPe-qGNvEaUgZyo2DVolm2q0dEP7wHG5HVh8nb6-TDMB0zxkngTostiN2Yl1JLhsFuu2K2Yx02vCiYRbW8e8z9OlzzkuB_tkZHPp3SCm_ADStlXxe8Cv3wFXPMZbz59CSafRCsk7C07kZC1BiWlEGVDGLiplbzTEbfWI_9PbUTPlGn07bONNQ5Ay0KnkhQeid6SpV5I4l6tVOM_XnVVyRzS9Uv0pHHRzTsqv4tWXVZ-zMmSYJjbBRKs183i8EmXyx1VHGPRQx0NodOzEcOFaCRDBRk-ZiitTPnZshIGN8ER-FxLm3o0LwIDT7Pb26X_0E93P-FgB0rSiyV1J6GmzagITtda5DVJxWt3nZgLS2cW5p5dG788ZO_c_MDNW9nlpfrqF166VHJe8CY8I3GXiiRhOF7KcUBKjKU7WAjM_5XA9R2hUPp2A_gA9Cyc3U9hxD-I6oJ4IZznGHany_sqEWV6TObG_RCcj_FfAHyq2sh8qbOoWpr2Y4y2c-_LquJ2mNhcsqAbFxhkX668y6xI0TbY1uRybF1aTuA1H37qZdU3vcTWbMg9BFZmJe04TtvFCgYrYe6JQuEwA1dZHk1RbQu1yMPEodZPCTFa--QkORQu9tzeBj9pBtm-UhRIH62DgvZ79kXki33rN3B0tv2mnk0I5d73fq_6VWUmfo-OZRZch1ajZsTGGrPD_1b2jDBNAUmmf-7Y1m4r8uIHUVfg_tvpXnv-5_PZcTApx6QP6EOMkMg6UBXUrlFyxmxKJ_YHYNI=w1920-h912)

![Pridiction ](https://lh3.googleusercontent.com/fife/ALs6j_HKGSw5IUMqzXZyY-4KcyEz9ref1Z6oaAe7uNMv0odAOvTBG1L2S2_qIMwdYxMMGzArBfSUlfXi0dG2ET8fzvZne-KjiZyx8C_6EufF9msUWlpaulcV2CK973KraVyjg5U65JvrjgaV4yLnliC2iPB5YeFDI5kIzcsv5R-eVgFedKgCsGaLYiKbM-IwDy8M-qGM2M7zf6AtLApzwGdonkUaRn30nwlv8Nw7XrEgkpLgI3kGOZGa4KWODESmAyR9BZkShX6aIkp1wE2SpECkqFD2CCTFrxkWqMzl9Zv2A2w0FRB-RgVagk-M-ruHNA0r0nMaF8y0vlE5PX6XJydspC1tUP-mYb_h4lyswsnm1b_KgswaA6feGiUXGXwTgefPQuvC4M14HzbEvOfxRHLAoVK3lM5cd-s0OlbnpOp2biscLtbFrgcbbWLhiZInywxvkW7WR1gtUYlfTUASMQxzfARcl4UzcawbkXwDW2DfrRkU1uigfPeGNnfOkIhX9aGKLglfLiam65WJsMBn64CjCWtojAQldJarkVkcp-hQnX2yBQ1W2uZmirzVlaamW74k_JR1JxMJxStURoYxEnD5vTVZwGJlsPuxDW0GqSwdQMzDKMhlFFlMKFY_NUgxABzOLXu8I4oIoOCaJsK9rVkKfl5Zrxop_caFpsLo73XYM1euetW75Zefi_Yo6i9JHdPi6uwTeURGVITFQMrbMsHffbTaSB2tGoBmWbYefW6zG6TKekVmXl5hSCckYtexbmRF0cBgiDa8lKTcRcUlPb52rlh_lMpU3Pr91BZe_fHEW1F2IFcPPuBSF6SMNzZoLiLydbMV00ruZWGrrb9PDAi4tIx63yI5sN-cgxHkPKj-IKxMrU22Xmc2cgsSIlGaE-U6P8mYSbTWEjUEt8fkGQFwY4gQ5vHBTgP75dy2ZPkVw4XZMSOVBQKXCbLGEcYWL-A7JkXQ3cogNaxieMvDU8rjmUH-KMoywnoAOVXIOTr0T6uyF4Jl8Ms4DX7OCW7F4xXEv7tzXrw6_iLR76chITBgyPifpvukAmiOLPWA3Suac7YlaowuucpAm8feVMwnBmYqcB4zNlMCYK6NDqn4a4MRJktMSYF---wxzpae5VRSebbrqXlTAMKtoborwZ9UtV-e_sF-udl8YPhisT4l05o9jix8xwYLCeULUkYpS17SeKNR0-s1Ng0xF7jUkoEuCUQ0xhf4Ka3hXrheBD9398vIlvU1KuNtVioqrEhrYyi7myY4kHNfYeY8JMiploKy2buv-0Kfo1Rt5SuOQW4O_dQdE78j1PQD0vS97jhl1IoJ7ddFmHvXNuX7POulNtzskQ3Pp9I3jlmCgVAwWRbmbXI4KWz4iQGyrD0ObC3pU-uZ4G_tJlirymqUdncXeG_EsOdZccu04Khlldi1aGWHQixGQnG8avth0F3hzWbh2UjFYSndjaaAxl77c5Cv-bz356p2W40uzeDW8VDtsmb2lWCpHwkoLM3PiZMK3yJ1N0zpNExBmCA3xU7Z1EFYgGQRhbIr5OFd5BTyq4x4siY9wzeN6qtcch2X7qP1-shzCHYox_ZVXhJ2F84-4XiTR8fuaT5gaJNVh7qCD7aGP1PSCLzTkw=w1920-h912)


---
📚 References

https://docs.google.com/document/d/1sYMr0zTlh6_cDVMLHkm12OwlmOoHkCLE/edit?usp=sharing&ouid=109017454699604670111&rtpof=true&sd=true

🚀 *Happy Coding!* 🌠

