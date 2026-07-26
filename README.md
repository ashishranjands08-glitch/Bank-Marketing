# Bank Marketing Subscription Predictor

A machine learning web app that predicts whether a bank customer is likely to subscribe to a **term deposit**, based on their profile and details from a marketing call. Trained on the [UCI Bank Marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing), served through a FastAPI backend, and presented through a custom-designed web form.

## ✨ Features

- **REST API** built with FastAPI for serving real-time predictions
- **Input validation** via Pydantic schemas, matching the model's expected features
- **Interactive web form** (`static/index.html`) — a self-contained, dependency-free HTML/CSS/JS page styled as a bank ledger, with dropdowns for categorical fields and live confidence scoring
- **Trained classifier** (scikit-learn, serialized with `joblib`) predicting subscription likelihood (`yes` / `no`) with a confidence score
- **Health check endpoint** for monitoring/deployment

## 🗂️ Project structure

```
.
├── app.py                  # FastAPI application & API routes
├── schema.py                # Pydantic request schema for /predict
├── Program.ipynb            # Data exploration & model training notebook
├── model/
│   └── bank_marketing_model.joblib   # Trained classifier
├── static/
│   └── index.html            # Frontend form (prediction UI)
├── requirements.txt
└── README.md
```

## 🔌 API Endpoints

| Method | Endpoint    | Description                                  |
|--------|-------------|-----------------------------------------------|
| GET    | `/`         | Serves the prediction form (`index.html`)     |
| GET    | `/health`   | Health check — returns `{"status": "ok"}`     |
| POST   | `/predict`  | Accepts customer/call details, returns a prediction |

### Example request

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "job": "admin.",
    "marital": "married",
    "education": "tertiary",
    "default": "no",
    "balance": 1000,
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "day": 15,
    "month": "may",
    "duration": 200,
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
  }'
```

### Example response

```json
{
  "prediction": "no",
  "confidence": 0.87
}
```

## 🧾 Input fields

| Field       | Type | Description                                              |
|-------------|------|------------------------------------------------------------|
| `age`       | int  | Customer's age                                             |
| `job`       | str  | Occupation category                                        |
| `marital`   | str  | Marital status: `married`, `single`, `divorced`            |
| `education` | str  | `primary`, `secondary`, `tertiary`, `unknown`               |
| `default`   | str  | Has credit in default? `yes` / `no`                         |
| `balance`   | int  | Average yearly account balance                              |
| `housing`   | str  | Has a housing loan? `yes` / `no`                             |
| `loan`      | str  | Has a personal loan? `yes` / `no`                            |
| `contact`   | str  | Contact method: `cellular`, `telephone`, `unknown`           |
| `day`       | int  | Day of month of last contact                                 |
| `month`     | str  | Month of last contact (`jan`–`dec`)                           |
| `duration`  | int  | Last contact duration, in seconds                            |
| `campaign`  | int  | Number of contacts during this campaign                      |
| `pdays`     | int  | Days since last contact from a previous campaign (`-1` = never contacted) |
| `previous`  | int  | Number of contacts before this campaign                      |
| `poutcome`  | str  | Outcome of the previous campaign: `unknown`, `failure`, `other`, `success` |

## 🚀 Getting started

### Prerequisites

- Python 3.13
- pip / venv

### Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd <repo-name>

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run locally

```bash
uvicorn app:app --reload
```

The app will be available at **http://127.0.0.1:8000/**.

- Fill out the form and submit to get a live prediction
- Visit `/health` to confirm the API is running
- Interactive API docs are available at `/docs` (FastAPI's built-in Swagger UI)

## 🧠 Model

The classifier was trained in `Program.ipynb` on the UCI Bank Marketing dataset, using the fields listed above as features and term-deposit subscription (`yes`/`no`) as the target. The trained pipeline is serialized to `model/bank_marketing_model.joblib` and loaded once at API startup.

## 🛠️ Tech stack

- **Backend:** FastAPI, Uvicorn
- **ML:** scikit-learn, pandas, joblib
- **Validation:** Pydantic
- **Frontend:** vanilla HTML/CSS/JS (no framework, no build step)

## 📄 License

Add your preferred license here (e.g. MIT).
