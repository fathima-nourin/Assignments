import os


class Endpoints:
    add_item_details = "/add_item_details"
    get_item_details = "/get_item_details"
    update_item_details = "/update_item_details/{item_id}"
    delete_item = "/delete_item/{item_id}"
    send_email = "/send_email"


class Email_constants:
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('MAIL_ID')
    smtp_password = os.getenv('MAIL_PASSWORD')
    print(smtp_username, smtp_password)

    # Set up the email content and recipient
    sender_email = 'fathimanourintr@gmail.com'
    subject = 'Data Email'
