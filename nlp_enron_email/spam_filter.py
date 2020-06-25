# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
import os

root_dir = "C:\\Users\\polgl\\Downloads\\enron_spam\\"

# loop over the directories
for directory, subdirectory, file_names in os.walk(root_dir):
    # include ham and spam folders only
    if not subdirectory:
        # prints directory, subdirectory and number of files
        print(directory, subdirectory, len(file_names))
        # TODO: read the files
