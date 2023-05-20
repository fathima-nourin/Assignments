from fastapi import FastAPI
import uvicorn
from scripts.services.inventory_service import router
from scripts.services import inventory_service

app = FastAPI()
app.include_router(inventory_service.router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=5673)
