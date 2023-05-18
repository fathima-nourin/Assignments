from scripts.core.handlers.calculate import Calculator
from scripts.schemas import CalculationInput
from fastapi import FastAPI
from scripts.services.site_report_service import router

app = FastAPI()
app.include_router(router)
calculator = Calculator()






