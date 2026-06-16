from fastapi import FastAPI, HTTPException
import numpy as np
from api.model_loader import model
from api.schema import ImageInput

# ✅ Prometheus imports
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response
import time

app = FastAPI()

# ✅ Metrics
REQUEST_COUNT = Counter("api_requests_total", "Total API Requests")
PREDICT_COUNT = Counter("predict_requests_total", "Total predictions made")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency")

@app.get("/")
def home():
    return {"message": "Model API running"}


@app.post("/predict")
def predict(data: ImageInput):
    REQUEST_COUNT.inc()
    start_time = time.time()

    if model is None:
        raise HTTPException(status_code=503, detail="Model not available")

    pixels = np.array(data.pixels)

    if pixels.ndim != 1:
        raise HTTPException(status_code=400, detail="`pixels` must be a flat list of numbers")

    if pixels.size != 64:
        raise HTTPException(status_code=400, detail="Expected 64 pixels for 8x8 image")

    X = pixels.reshape(1, -1)
    pred = int(model.predict(X)[0])

    PREDICT_COUNT.inc()

    # ✅ Record latency
    REQUEST_LATENCY.observe(time.time() - start_time)

    return {"prediction": pred}


# ✅ Prometheus endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")