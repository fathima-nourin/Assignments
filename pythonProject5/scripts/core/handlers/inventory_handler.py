from scripts.utils.mongo_utility import Mongoserver
from scripts.core.handlers.mqtt_pub import Publisher
from scripts.db.mongodb import Aggregate
import smtplib
from scripts.constants.app_constants import Email_constants
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # construct mail with multipart


class InventoryHandler:

    def __init__(self):
        self.mongo_server_obj = Mongoserver()

    # def add_item(self, item_id: int, item: dict):
    #
    #     existing_item = self.mongo_server_obj.check_item(item_id)
    #     if existing_item:
    #         return {"message": "Item already exists in the inventory."}
    #     else:
    #         self.mongo_server_obj.write_items(item)
    #         return {"message": "Item added successfully"}
    def add_item(self, item_id: int, item: dict):

        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            if item.get("update", True):
                response = self.mongo_server_obj.update_details(item_id, item)
                if response:
                    if item_id is not None:
                        data = list(self.mongo_server_obj.read_items(query={"id": item_id},
                                                                     filter_dict={"_id": 0}))
                        return {"item updated"}
                        # return data
            else:
                return {"item cannot be updated"}
            # else:
            #     return {"message": "Item already exists in the inventory."}
        else:
            self.mongo_server_obj.write_items(item)
            return {"message": "Item added successfully"}

    def get_item(self, item_id):
        # find_item =self.mongo_server_obj.find_one({"id"=1})

        try:
            query = {}
            if item_id is not None:
                query = {"id": item_id}
            data = list(self.mongo_server_obj.read_items(query=query,
                                                         filter_dict={"_id": 0}))
            return data
        except Exception as e:
            raise Exception(str(e))

    def update_item(self, item_id: int, updated_item: dict):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            if updated_item.update:
                result = self.mongo_server_obj.update_details(item_id, updated_item)
        if result.modified_count == 1:
            return {"message": "Item updated successfully", "update": True}
        else:
            return {"message": "Item not found", "update": False}

    # def update_item(self, item_id: int, updated_item: dict):
    #     condition = {"$and": [{'id': item_id}, {"update": True}]}
    #     result = self.mongo_server_obj.update_on_condition(condition, updated_item)
    #     if result.modified_count == 1:
    #         return {"message": "Item updated successfully", "update": True}
    #     else:
    #         return {"message": "Item not found", "update": False}

    def delete_item(self, item_id: int):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            result = self.mongo_server_obj.delete_items(item_id)
            if result.deleted_count == 1:
                return {"message": "Item deleted successfully"}
            else:
                return {"message": "Item not found"}
        return {"message": "item not found"}

    def pick_item(self, item_id: int):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            # inventory[item_id]["count"] += 1
            publisher = Publisher(host="localhost", port=1883, topic='pick-count')
            print(existing_item)
            existing_item["count"] += 1
            existing_item["quantity"] -= 1
            self.mongo_server_obj.update_details(item_id, {"count": existing_item["count"],
                                                           "quantity": existing_item["quantity"]})
            publisher.publish(f"item_id:{item_id}, count: {existing_item['count']}")
            return {
                "message": f"Item {item_id} has been picked {existing_item['count']} times,the number of items left is {existing_item['quantity']}"}
        else:
            return {"message": "item doesnot exist"}

    def send_aggregatemail(self, recv_email):
        data = self.mongo_server_obj.aggregate_data(Aggregate.aggr)
        total_cost = data[0]['total']

        # total_item_cost = [i for i in self.mongo_server_obj.aggregate_data(total_cost)]
        # return total_item_cost
        # code for sending mail
        try:
            message = '''
                      Hello,
    
                      Here is the total cost of the items in the inventory:
    
                      
    
                      TOTAL COST OF ITEMS={}
                      Best regards,
                      Fathima Nourin T R,
                      '''.format(total_cost)
            # format(table, total_cost)
            email = MIMEMultipart()
            email['From'] = Email_constants.smtp_username
            email['To'] = recv_email
            email['Subject'] = Email_constants.subject
            # Attach the message to the email
            email.attach(MIMEText(message, 'plain'))
            # Connect to the SMTP server and send the email
            server = smtplib.SMTP(Email_constants.smtp_server, Email_constants.smtp_port)
            server.starttls()  # to enable a secure communication channel using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption
            server.login(Email_constants.smtp_username, Email_constants.smtp_password)  # authentication
            server.send_message(email)
            # print('Email sent successfully.')
            return {"message": "Email sent successfully."}
            server.quit()
        except smtplib.SMTPException as e:
            return {"message": "Failed to send email. Exception: {}".format(str(e))}


inventory_obj = InventoryHandler()
