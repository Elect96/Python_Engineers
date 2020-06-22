# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
import os

root_dir = "C:\\Users\\polgl\\Downloads\\enron_mail\\maildir\\lay-k"

# loop over the directories
for directory, subdirectory, file_names in os.walk(root_dir):
    # prints directory, subdirectory and number of files
    print(directory, subdirectory, len(file_names))
