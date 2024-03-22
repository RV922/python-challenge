import os 
import csv

# Set the path for the csv file where the data set is laid

csvpath = os.path.join('.','Resources','election_data.csv')

# Opens up the file for that path utilizing "," as a delimeter for each column and skips the header

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)

# This first loop counts the total number of votes in the dataset

    total_votes = 0
    list_of_candidates = []

    for row in csvreader:
        total_votes += 1

# The second loop returns a list with all the candidate names that participated in the election
        
        candidate_name = row[2]
        if candidate_name not in list_of_candidates: 
            list_of_candidates.append(candidate_name)

# The third loop calculates the total number of votes that each candidate got and then 
# calculates the percentage of votes each candidate won in the election   

# Reopens the file once again to utilize a different loop            
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
        
    candidate1 = list_of_candidates[0]
    candidate2 = list_of_candidates[1]
    candidate3 = list_of_candidates[2]
    votes_for_candidate1 = 0
    votes_for_candidate2 = 0
    votes_for_candidate3 = 0
    
    for row in csvreader:
        if row[2] == candidate1:
            votes_for_candidate1 += 1
        
        elif row[2] == candidate2:
            votes_for_candidate2 += 1

        else:
            votes_for_candidate3 += 1
            
    percentage_for_candidate1 = round(((votes_for_candidate1/total_votes)*100),3)
    percentage_for_candidate2 = round(((votes_for_candidate2/total_votes)*100),3)
    percentage_for_candidate3 = round(((votes_for_candidate3/total_votes)*100),3)

# The fourth loop returns the winner of the election (Candidate with the most votes)

    votes_by_candidates = []
    votes_by_candidates.append(votes_for_candidate1)
    votes_by_candidates.append(votes_for_candidate2)
    votes_by_candidates.append(votes_for_candidate3)
    most_votes = 0
    candidate_most_voted = ''

# Creates a dictionary by fusing the list of all candidates (Keys) and the list of votes for each candidate (Values)
    votes_per_candidates = dict(zip(list_of_candidates, votes_by_candidates))

    for candidates, votes in votes_per_candidates.items():
        if votes > most_votes:
            most_votes = votes
            candidate_most_voted = candidates

# Printing

print("Election Results")

print("-----------------------")

# Print total number of votes calculated in the first loop
print(f"Total votes: {total_votes}")

print("-----------------------")

# Print the names of all candidates that participated in the election, calculated in the second loop 
    
print("The candidates are:")
print(f"{list_of_candidates}")
    
# Print the total amount of votes that each candidate got with their corresponding percentage in the election, 
#calculated in the third loop
        
print(f"{candidate1}: {percentage_for_candidate1}% ({votes_for_candidate1})")
print(f"{candidate2}: {percentage_for_candidate2}% ({votes_for_candidate2})")
print(f"{candidate3}: {percentage_for_candidate3}% ({votes_for_candidate3})")

print("-----------------------")

# Print the winner of the election (candidate with the most votes), calculated in the fourth loop
print(f"The winner is: {candidate_most_voted}")

print("-----------------------")



# Exporting Results

# Set path for output file
output_txt = os.path.join(".","Analysis","Analysis.txt")

# Open the output file
with open(output_txt,'w') as txtfile:


    # Printing

    txtfile.write("Election Results\n")

    txtfile.write("-----------------------\n")

    # Print total number of votes calculated in the first loop
    txtfile.write(f"Total votes: {total_votes}\n")

    txtfile.write("-----------------------\n")

    # Print the names of all candidates that participated in the election, calculated in the second loop 
        
    txtfile.write("The candidates are:\n")
    txtfile.write(f"{list_of_candidates}\n")
        
    # Print the total amount of votes that each candidate got with their corresponding percentage in the election, 
    #calculated in the third loop
            
    txtfile.write(f"{candidate1}: {percentage_for_candidate1}% ({votes_for_candidate1})\n")
    txtfile.write(f"{candidate2}: {percentage_for_candidate2}% ({votes_for_candidate2})\n")
    txtfile.write(f"{candidate3}: {percentage_for_candidate3}% ({votes_for_candidate3})\n")

    txtfile.write("-----------------------\n")

    # Print the winner of the election (candidate with the most votes), calculated in the fourth loop
    txtfile.write(f"The winner is: {candidate_most_voted}\n")

    txtfile.write("-----------------------\n")
