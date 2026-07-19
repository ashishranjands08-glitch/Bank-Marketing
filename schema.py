from pydantic import BaseModel

class BankMarketingSchema(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

    model_config = {
        "json_schema_extra": {
            "example": {
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
            }
        }
    }