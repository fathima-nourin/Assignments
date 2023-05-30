import os
import yaml
from constants import Constants


def verify_credentials(userinput_username, userinput_password):
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    stored_username = config.get('username')
    stored_password = config.get('password')
    if userinput_username == stored_username and userinput_password == stored_password:
        return True, "credentials matched"
    elif userinput_username != stored_username:
        return False, "invalid username"
    elif userinput_password != stored_password:
        return False, "incorrect password"


def start_reading():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    file_to_be_read = config.get('file_to-be_read')
    print(file_to_be_read)
    lines = read_file(file_to_be_read)
    if lines is not None:
        read = config.get('no_read_lines')
        read_lines(lines, read)
    else:
        print("File does not exist.")


# def start_reading():
#     with open('config.yaml', 'r') as config_file:
#         config = yaml.safe_load(config_file)
#     files = config['files']
#     for file_name in files:
#         new_file = input("enter the file to be read: ").lower()
#         lines = read_file(new_file)
#         if lines is not None:
#             read = int(input("Number of lines to be read: "))
#             read_lines(lines, read)
#         else:
#             print("File does not exist.")


def read_file(file_name):
    if os.path.exists(file_name):
        with open(f"{file_name}", "r") as file:
            lines = file.readlines()
            return lines
    else:
        return None


def read_lines(lines, read):
    end_index = len(lines)
    if read > end_index:
        for line in lines:
            print(line)
        print("end of the file")
    else:
        no_of_operation = end_index // read
        start = 0
        end = min(start + read, end_index)
        line_num = 0
        while no_of_operation > 0:
            for line in lines[start:end]:
                print(line)
            if end == end_index:
                print("Completed reading.")
                break
            line_num += read
            remaining_lines = end_index - line_num
            try:
                user_input = input("Continue reading? (yes/no): ")
                if user_input.lower().strip() == "yes":
                    start += read
                    end = min(start + read, end_index)
                    if remaining_lines < read:
                        start = line_num
                        end = end_index
                        for line in lines[start:end]:
                            print(line)
                        print("Completed reading.")
                else:
                    raise ValueError("Invalid input")
            except ValueError as e:
                print("Reading paused:", e)
                break
            no_of_operation -= 1

# def inputting():
# read = int(input("Number of lines to be read: ")
# return read
