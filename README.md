# 🔥 CaloriBurn — Calorie Burn Prediction App

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

A machine learning web application that predicts the number of calories burned during exercise based on personal physiological data. Built with FastAPI as the backend and a custom-designed HTML/CSS/JS frontend.

🔗 **Live Demo:** [calorie-burn-prediction-production.up.railway.app](https://calorie-burn-prediction-production.up.railway.app/)

📓 **Kaggle Notebook:** [Calories Burnt Prediction — XGBR, GBR, SVR, CBR](https://www.kaggle.com/code/muktiprabowo/calories-burnt-prediction-xgbr-gbr-svr-cbr)

---

## 📸 Preview

![CaloriBurn Preview](https://raw.githubusercontent.com/muktiprab/calorie-burn-prediction/Source-Code-and-Preview/CaloBurn%20Preview.png)

---

## 🚀 Features

- Predict calories burned based on physiological input
- Responsive split-screen UI with animated result display
- Dynamic feedback tags (Light Activity, Cardio Zone, Elite Performance, etc.)
- Input validation with max duration constraint based on training data range
- REST API endpoint ready for integration

---

## 🧠 Machine Learning

Three regression models were trained and compared:

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| XGBoost Regressor | 0.9986 | 1.5521 | 2.2966 |
| CatBoost Regressor | 0.9997 | 0.5225 | 0.9275 |
| **SVR (RBF Kernel)** | **0.9999** | **0.3090** | **0.6126** |

**Best model: Support Vector Regression (SVR)** with StandardScaler preprocessing via sklearn Pipeline.

### Model Parameters
```python
Pipeline([
    ('scaler', StandardScaler()),
    ('model', SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1))
])
```

### Features Used
| Feature | Type | Description |
|---|---|---|
| Gender | int | 0 = Female, 1 = Male |
| Age | float | Age in years |
| Height | float | Height in cm |
| Weight | float | Weight in kg |
| Duration | float | Exercise duration (max 30 min) |
| Heart_Rate | float | Heart rate in bpm |
| Body_Temp | float | Body temperature in °C |

---

## 🗂️ Project Structure

```
calorie-burnt/
├── main.py            # FastAPI backend
├── index.html         # Frontend UI
├── svr_model.pkl      # Trained model
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
└── README.md
```

---

## ⚙️ Installation & Usage

### 1. Clone repository
```bash
git clone https://github.com/muktiprab/calorie-burn-prediction.git
cd calorie-burn-prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m uvicorn main:app --reload
```

Open `http://localhost:8000` in your browser.

---

## 🐳 Docker

```bash
# Build image
docker build -t caloriburn .

# Run container
docker run -p 8000:8000 caloriburn
```

---

## 📡 API Endpoint

### `POST /predict`

**Request body:**
```json
{
  "Gender": 1,
  "Age": 25,
  "Height": 175.0,
  "Weight": 70.0,
  "Duration": 20.0,
  "Heart_Rate": 110.0,
  "Body_Temp": 37.5
}
```

**Response:**
```json
{
  "calories": 183.47
}
```

---

## ⚠️ Limitations

- Model is trained on exercise duration up to **30 minutes**. Predictions outside this range may not be reliable (extrapolation).
- Model was trained with scikit-learn 1.6.1 — minor version differences may produce warnings but do not affect predictions.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Uvicorn, Pydantic
- **ML:** scikit-learn, NumPy, joblib
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Docker, Railway

---

## 👤 Author

**Mukti Prabowo**
- GitHub: [@muktiprab](https://github.com/muktiprab)
- LinkedIn: [muktiprabowo](https://linkedin.com/in/muktiprabowo)
- Kaggle: [@muktiprab007](https://www.kaggle.com/muktiprabowo)
