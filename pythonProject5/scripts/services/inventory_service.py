from typing import List

from fastapi import APIRouter
from scripts.schemas import Inventory
from scripts.schemas import Email, ResponseModel
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


@router.get(Endpoints.get_item_details, response_model=List[ResponseModel])
def get_items():
    try:
        return inventory_handler.get_item(None)
    except Exception as e:
        print("error in getting_items", str(e))


@router.get(Endpoints.get_item_details + "/{item_id}", response_model=list[ResponseModel])
def get_item(item_id: int):
    try:
        return inventory_handler.get_item(item_id=item_id)
    except Exception as e:
        print(e.args)


@router.put(Endpoints.update_item_details)
def update_items(inventory: Inventory):
    try:
        return inventory_handler.update_item(item_id=inventory.id, updated_item=inventory.dict())
    except Exception as e:
        print("error in updating items", str(e))


@router.delete(Endpoints.delete_item)
def delete_items(item_id: int):
    try:
        return inventory_handler.delete_item(item_id=item_id)
    except Exception as e:
        print("error in deleting items", str(e))


@router.get(Endpoints.pick_count)
def increment_count(item_id:int):
    try:
        return inventory_handler.pick_item(item_id)
    except Exception as e:
        print("error in picking the item", str(e))
    # global base_count
    # base_count += 1
    # return {'count': base_count}


@router.post(Endpoints.send_email)
def send_email(email: Email):
    try:
        return inventory_handler.send_aggregatemail(email.email)
    except Exception as e:
        print("error in sending mail", str(e))
