import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from schema import BankMarketingSchema

app = FastAPI(
    title="Bank Marketing API",
    description="API for predicting bank marketing outcomes",
    version="1.0.0"
)

# Serve any additional static assets (css/js/images) placed under static/
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("model/bank_marketing_model.joblib")

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: BankMarketingSchema):
    input_data = pd.DataFrame([data.model_dump()])
    raw_prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]
    class_index = list(model.classes_).index(raw_prediction)
    confidence = float(proba[class_index])
    label = str(raw_prediction)
    return {
        "prediction": label,
        "confidence": confidence
    }