# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
import os
from email.parser import Parser


# extracts the data from an email
def email_analyse(input_file, e_to, e_from, e_body):
    # open and close the file handle
    with open(input_file, "r") as f:
        data = f.read()
    # parse the data
    email = Parser().parsestr(data)
    # access the data
    e_to.append(email['to'])
    e_from.append(email['from'])
    e_body.append(email.get_payload())


# root directory
root_dir = "C:\\Users\\polgl\\Downloads\\enron_mail\\maildir\\lay-k"
# email variables
email_to_list = []
email_from_list = []
email_body_list = []

# loop over the directories
for directory, subdirectory, file_names in os.walk(root_dir):
    # loop over the files in respective directories
    for file_name in file_names:
        # analyse emails
        email_analyse(os.path.join(directory, file_name), email_to_list, email_from_list, email_body_list)

# write email_to_list to a file
with open("email_to_list.txt", "w")as f:
    for email_to in email_to_list:
        if email_to:
            f.write(email_to)
            f.write("\n")

# write email_from_list to a file
with open("email_from_list.txt", "w")as f:
    for email_from in email_from_list:
        if email_from:
            f.write(email_from)
            f.write("\n")

# write email_body_list to a file
with open("ken_lay_emails.txt", "w")as f:
    for email_body in email_body_list:
        if email_body:
            f.write(email_body)
            f.write("\n")
