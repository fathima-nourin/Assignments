from scripts.utils.mongo_utility import Mongoserver
from scripts.db.mongodb import Aggregate
import smtplib
from scripts.constants.app_constants import Email_constants
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # construct mail with multipart


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

    def send_aggregatemail(self, recv_email):
        data = self.mongo_server_obj.aggregate_data(Aggregate.aggr)
        total_cost = data[0]['total']
        # total_item_cost = [i for i in self.mongo_server_obj.aggregate_data(total_cost)]
        # return total_item_cost
        # code for sending mail
        message = '''
                  Hello,

                  Here is the total cost of the items in the inventory:

                  

                  TOTAL COST OF ITEMS={}
                  Best regards,
                  Fathima Nourin T R,
                  '''.format(total_cost)
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
