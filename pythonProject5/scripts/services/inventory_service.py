from fastapi import FastAPI
from fastapi import APIRouter
from scripts.schemas import Inventory
from scripts.core.handlers.inventory_handler import InventoryHandler
from scripts.constants.app_constants

router = APIRouter()

inventory_handler = InventoryHandler()


@router.post("/add_item_details")
def add_items(inventory: Inventory):
    try:
        return inventory_handler.add_item(item_id=inventory.id, item=inventory.dict())
    except Exception as e:
        print("error in add_items", str(e))


@router.get(Endpoints.get_item_details")
def get_items():
    print("service")
    return inventory_handler.get_item()


@router.put("/update_item_details/{item_id}")
def update_items(inventory: Inventory):
    return inventory_handler.update_item(item_id=inventory.id, updated_item=inventory.dict())


@router.delete("/delete_item/{item_id}")
def delete_items(item_id:int):
    return inventory_handler.delete_item(item_id=item_id)
