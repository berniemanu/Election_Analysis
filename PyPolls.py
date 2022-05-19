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

# Initialize dictionary where candidates and 
# their respective votes will be stored.
candidate_votes={}

# to compare and find the winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open function to open the csv file to read
with open(file_to_load) as election_data:

    #To read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    # to skip the header row.
    headers = next(file_reader)

    # loop through each row in the CSV file to count total votes and get candidates list
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
 
# to save results to a text file.
with open(file_to_save, "w") as txt_file:

    # print the final count to the terminal.
    election_results = (
        f"Election Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")

  # Save the final count to the text file.
    txt_file.write(election_results)

    # to iterate through the dictionary and pull out 
    # every candidate and their % of vote.
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:0.1f}% ({votes:,}).\n")
        
        # to print individual candidate results in the terminal.
        print(candidate_results)
        
        # to save individual candidate results to the text file
        txt_file.write(candidate_results)

        if winning_count < votes and winning_percentage < vote_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
           
    # print and save winning_candidate_summary
    winning_candidate_summary = (f"\nWinner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:0.1f}%\n")
    txt_file.write(winning_candidate_summary)
print(winning_candidate_summary)








