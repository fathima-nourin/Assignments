from test import start_reading, verify_credentials
import yaml

if __name__ == '__main__':

    userinput_username = input("enter the username : ")
    userinput_password = input("enter the password : ")

    credentials_result, credentials_statement = verify_credentials(userinput_username, userinput_password)
    print(credentials_statement)
    if credentials_result:
        print("logged in")
        start_reading()
    else:
        print("try again")
