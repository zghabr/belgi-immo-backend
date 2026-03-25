from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from PropertyData import Property
from predictionService import get_prediction
from statService import get_stats_data

app = FastAPI(title="BelgiImmo Prediction API")

# --- CORS Middleware ---
# Allow all origins for development; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "BelgiImmo Real Estate Prediction API is running"}


@app.get("/stats")
async def get_stats():
    """
    Get comprehensive market statistics for the dashboard.
    """

    # In a real application, these would be computed from the dataset
    return get_stats_data()


@app.post("/predict")
async def predict(data: Property):
    """
    Predict the price of a property based on its features.
    """

    print(f"Received data for prediction: {data}")
    try:
        prediction = get_prediction(data)
        return {
            "status": "success",
            "prediction": round(float(prediction), 2),
            "currency": "EUR",
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
