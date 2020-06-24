# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
import os
from email.parser import Parser
import Counter


# extracts the data from an email
def email_analyse(input_file, e_to, e_from, e_body):
    # open and close the file handle
    with open(input_file, "r") as f:
        data = f.read()
    # parse the data
    email = Parser().parsestr(data)
    # data handling
    if email['to']:
        e_to = email['to']
        # remove all \n, \t and empty spaces
        e_to = e_to.replace("\n", "").replace("\t", "").replace(" ", "")
        # extract individual emails
        e_to = e_to.split(",")
        # transform emails list into individual instances
        for element in e_to:
            email_to_list.append(element)
    e_from.append(email['from'])
    e_body.append(email.get_payload())


# root directory
root_dir = "C:\\Users\\polgl\\Downloads\\enron_mail\\maildir\\lay-k\\family"
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

print("Top 10 most common addressee:", Counter(email_to_list).most_common(10))
print("Top 10 most common addresser:", Counter(email_from_list).most_common(10))

# fix PyCharm's import counter error https://www.youtube.com/watch?v=RvbUqf3Tb1s
