from pymongo import MongoClient


# from scripts.constants import Aggregate
# import json


class Mongoserver:

    def __init__(self):
        try:
            self.client_uri = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
            self.db = "interns_b2_23"
            self.collection = "nourin"
        except Exception as e:
            raise Exception(str(e))

    def check_item(self, item_id):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.find_one({"id": item_id})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def write_items(self, item):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.insert_one(item)
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def read_items(self, query: dict = {}, filter_dict: dict = {}):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.find(query, filter_dict)
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def update_details(self, item_id, updated_item):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.update_one({"id": item_id}, {"$set": updated_item})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def update_on_condition(self, condition, updated_item):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            result = mongo_collect.update_one(condition, {'$set': updated_item})
            print(updated_item)
            return result
        except Exception as e:
            raise Exception(str(e))

    def delete_items(self, item_id):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.delete_one({"id": item_id})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def aggregate_data(self, pipeline: list):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = list(mongo_collect.aggregate(pipeline))
            return mongo_result
        except Exception as e:
            raise Exception(str(e))
