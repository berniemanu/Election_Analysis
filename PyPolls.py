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

# Initialize total vote counter/accumulator
total_votes=0

# Initializee the list of candidates.
candidate_options=[]

#Initialize dictionary
candidate_votes={}

# to compare and find the winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open function to open the file as a text file to write in it
with open(file_to_load) as election_data:

    #To read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Count each row in the CSV file.
    for row in file_reader:
        # To get the candidate names
        candidate_name=row[2]

        # Increase the total_votes counter by 1
        total_votes +=1

        # Check if the candidates name is already in the list.
        if candidate_name not in candidate_options:

            # Add the candidate name to candidate options list.
            candidate_options.append(candidate_name)

            # Begin tracking votes for the candidate.
            candidate_votes[candidate_name]=0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name]+=1

# Print candidates list.
# print(candidate_votes)

# to iterate through the dictionary and pull out every candidate and their % of vote.
for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:0.1f}% ({votes:,}).")

    if winning_count < votes and winning_percentage < vote_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

candidate_votes[candidate_name]+=1

print(f"\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:0.1f}%\n")








