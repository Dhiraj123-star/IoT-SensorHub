from fastapi import FastAPI
from app.routers import api

app = FastAPI(title="IoT Sensor Monitoring System")

app.include_router(api.router)
