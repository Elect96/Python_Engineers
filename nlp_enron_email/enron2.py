# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
from email.parser import Parser

# file to read location
file_to_read = "C:\\Users\\polgl\\Downloads\\enron_mail\\maildir\\lay-k\\all_documents\\1_"

# open and close the file handle
with open(file_to_read, "r") as f:
    data = f.read()

# parse the data
email = Parser().parsestr(data)

# access the data
print("\nTo:", email['to'])
print("From:", email['from'])
print("Subject:", email['subject'])
print("\nBody:", email.get_payload())
