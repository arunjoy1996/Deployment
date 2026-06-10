import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_home():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.get("/")
        assert res.status_code == 200

@pytest.mark.asyncio
async def test_predict():
    dummy = {"pixels": [0.0]*784}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/predict", json=dummy)
        assert res.status_code == 200