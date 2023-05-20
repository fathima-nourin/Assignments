from scripts.utils.mongo_utility import Mongoserver


class InventoryHandler:
    def __init__(self):
        self.mongo_server_obj = Mongoserver()

    def add_item(self, item_id: int, item: dict):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            return {"message": "Item already exists in the inventory."}
        else:
            self.mongo_server_obj.write_items(item)
            return {"message": "Item added successfully"}

    def get_item(self):
        data = list(self.mongo_server_obj.read_items())
        for items in data:
            del items['_id']
        return data

    def update_item(self, item_id: int, updated_item: dict):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            result = self.mongo_server_obj.update_details(item_id, updated_item)
            if result.modified_count == 1:
                return {"message": "Item updated successfully"}
            else:
                return {"message": "Item not found"}
        return {"message": "item not found"}

    def delete_item(self, item_id: int):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            result = self.mongo_server_obj.delete_items(item_id)
            if result.deleted_count == 1:
                return {"message": "Item deleted successfully"}
            else:
                return {"message": "Item not found"}
        return {"message": "item not found"}
