# Contents of /ai-property-management-assistant/ai-property-management-assistant/backend/src/main.py

from fastapi import FastAPI
from api.routes import properties, tenants, maintenance, auth

app = FastAPI()

app.include_router(properties.router)
app.include_router(tenants.router)
app.include_router(maintenance.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Property Management Assistant API"}