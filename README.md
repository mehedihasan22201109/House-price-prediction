<<<<<<< HEAD
# 🏡 USA House Price Prediction & Deployment Platform

An end-to-end Machine Learning project that performs Exploratory Data Analysis (EDA), builds highly optimized regression pipelines, and deploys the champion model through an interactive Gradio web application interface.

## 📊 Dataset Insights & Architecture
The predictive system is trained on regional housing statistics across 5 key numerical features:
- **Avg. Area Income**: Average annual income of area residents.
- **Avg. Area House Age**: Average age of houses in the locality.
- **Avg. Area Number of Rooms**: Mean room count per household.
- **Avg. Area Number of Bedrooms**: Mean bedroom count per household.
- **Area Population**: Total population density of the region.

## 📈 Model Performance Evaluation
We evaluated multiple predictive pipelines packed with standard preprocessing layers (`StandardScaler`). The models achieved the following metrics:

| Model Pipeline | Train \(R^2\) | Test \(R^2\) | Test MSE | Status |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Regression** | **0.9192** | **0.9176** | **10,089,009,301** | **🏆 Champion** |
| Ridge Regression | 0.9192 | 0.9176 | 10,089,010,042 | Stable |
| Lasso Regression | 0.9192 | 0.9176 | 10,089,009,322 | Stable |
| Polynomial + Ridge | 0.9205 | 0.9157 | 10,323,248,311 | Overfitted |
| KNN Regressor (k=9) | 0.8920 | 0.8804 | 14,635,282,109 | Baseline |

## 🛠️ Installation & Execution

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd House_Price-Deployment
   ```

2. **Environment Activation & Setup:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

3. **Launch Live Interface:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:7860` in your web browser.

## 📁 Repository Structure
```text
.
├── data/
│   └── USA_Housing.csv
├── models/
│   └── best_model.pkl
├── notebooks/
│   ├── 1_eda.ipynb
│   └── 2_training.ipynb
├── screenshots/
│   ├── price_distribution.png
│   ├── price_scatter_plots.png
│   ├── correlation_heatmap.png
│   └── gradio_ui.png
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```
=======
# House-price-prediction
>>>>>>> 01b52260c16659fab0c641410fc855ba96d08c0b
