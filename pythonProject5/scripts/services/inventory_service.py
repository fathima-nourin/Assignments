from fastapi import APIRouter
from scripts.schemas import Inventory
from scripts.schemas import Email
from scripts.core.handlers.inventory_handler import InventoryHandler
from scripts.constants.app_constants import Endpoints

router = APIRouter()

inventory_handler = InventoryHandler()


@router.post(Endpoints.add_item_details)
def add_items(inventory: Inventory):
    try:
        return inventory_handler.add_item(item_id=inventory.id, item=inventory.dict())
    except Exception as e:
        print("error in add_items", str(e))


@router.get(Endpoints.get_item_details)
def get_items():
    print("service")
    return inventory_handler.get_item()


@router.put(Endpoints.update_item_details)
def update_items(inventory: Inventory):
    return inventory_handler.update_item(item_id=inventory.id, updated_item=inventory.dict())


@router.delete(Endpoints.delete_item)
def delete_items(item_id: int):
    return inventory_handler.delete_item(item_id=item_id)


@router.post(Endpoints.send_email)
def send_email(email: Email):
    return inventory_handler.send_aggregatemail(email.email)
