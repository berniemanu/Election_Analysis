# 1. Count the total number of votes.
# 2. Collect the list of all candidates.
# 3. Count votes for each candidates.
# 4. Calculate votes % for each candidate.
# 5. Declare the candidate with highest vote % as the winner.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open function to open the file as a text file to write in it
with open(file_to_load) as election_data:

    #To read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)




