import yaml
import os
from constants import Constants
from test import read_file, read_lines

if __name__ == '__main__':
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    files = config['files']
    for file_name in files:
        constant_obj = Constants()
        new_file = input("enter the file to be read: ").lower()
        lines = read_file(new_file)
        if lines is not None:
            # read = int(input("Number of lines to be read: "))
            # read_lines(lines,read)
            read_lines(lines, constant_obj.inputting())
        else:
            print("File does not exist.")

# with open(file_name, 'r') as file:
#
#     file_contents = file.read()
#     print(file_contents)

# try:
#     new_file = open("file.log", 'r')
# except FileNotFoundError:
#     print("Error: File does not appear to exist.")
# try:
#     if new_file:
#         lines = new_file.readlines()
#
#         end_index = len(lines)
#         # print(end_index)
#         read = int(input("number of lines to be read :"))
#         no_of_operation = end_index // read
#         start = 0
#         end = min(start + read, end_index)
#         line_num = 0
#         for i in range(no_of_operation):
#             for line in lines[start:end]:
#                 print(line)
#             if end == end_index:
#                 break
#             line_num += read
#             # print(line_num)
#             remaining_lines = end_index - line_num
#             user_input = input("continue reading :")
#             if user_input.lower().strip() == "yes":
#                 start += read
#                 end = min(start + read, end_index)
#             else:
#                 break
#         if remaining_lines < read:
#             start = line_num
#             end = end_index
#             for line in lines[start:end]:
#                 print(line)
#
#         print("completed reading")
#         new_file.close()
# except FileNotFoundError:
#     print("Couldnot read the file")
#
# new_file.close()
