#import os and csv module
import os
import csv

#read csv
csvpath = r"C:\Users\Güero\Desktop\python-challenge\PyPoll\Resources\election_data.csv"
print(csvpath)

#make variables
total_votes = []
stockham_votes = []
degette_votes = []
doane_votes = []

#open csv and encode
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #ignore headers
    csv_header = next(csvreader)
    for row in csvreader:
        #count number of votes
        total_votes.append(row[0])
        #count votes for candidates
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1

#make dict to find winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]

#zip to pair candidates with votes and get max to see the winner
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

#make variable for total votes as integer
total_vote_count = len(total_votes)

#calculate percentage of votes
stockham_percentage = (stockham_votes/total_vote_count) * 100
degette_percentage = (degette_votes/total_vote_count) * 100
doane_percentage = (doane_votes/total_vote_count) * 100

#print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes : {len(total_votes)}")
print("--------------------------")

#print percentage of votes
print(f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percentage:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#make text file
analysis = os.path.join("Analysis", "ElectionAnalysis.txt")
with open(analysis,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}" )
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percentage:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")