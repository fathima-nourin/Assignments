from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from scripts.services.inventory_service import router
from scripts.services import inventory_service

app = FastAPI()
app.include_router(inventory_service.router)

if __name__ == '__main__':
    load_dotenv()
    uvicorn.run("main:app", port=5673, reload=True)
