from fastapi import FastAPI, HTTPException
import numpy as np
from api.model_loader import model
from api.schema import ImageInput
import os

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Model API running"}


@app.post("/predict")
def predict(data: ImageInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")

    pixels = np.array(data.pixels)
    print("Min:", pixels.min(), "Max:", pixels.max())
    print("Prediction input sum:", float(pixels.sum()))
    print(pixels[:10])
    if pixels.ndim != 1:
        raise HTTPException(status_code=400, detail="`pixels` must be a flat list of numbers")

    # Expecting sklearn digits (8x8) flattened = 64 features
    if pixels.size != 64:
        raise HTTPException(status_code=400, detail="Expected 64 pixels for 8x8 image (digits dataset)")

    X = pixels.reshape(1, -1)
    pred = int(model.predict(X)[0])
    return {"prediction": pred}
