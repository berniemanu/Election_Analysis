# Election Analysis

## Project Overview

### Initial Project Overview:
A Colorado Board of Elections employee Tom and his manager Seth wanted my help in analysing and completing an audit of a recent local congressional election.
Instead of doing an excel analysis, Seth and Tom wanted to automate the task using Python. They primarily needed the following tasks to be completed for their election audit.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Challenge Project Overview:
Following the successful completion of initial report, the election commission had requested the following additional data to complete the audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

I had to write python code to initialize new variables, count votes per county and compare votes between different counties and pick the county with largest voters turnout.

## Resources:
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.67.1

## Election Audit Results:
The analysis of the election show that:
- There were total 369,711 votes cast in the election.
- The counties were the elections where held were:
    - Jefferson
    - Denver
    - Arapahoe
- Counties' election results were:
    - Jefferson County received 10.5% of the vote and 38,855 number of votes.
    - Denver County received 82.8% of the vote and 306,055 number of votes.
    - Arapahoe County received 6.7% of the voteand 24,801 number of votes.
- And the county with the largest turnover is:
    - Denver, which received more than 80% of total votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary: 
Automating CSV file analysis using Python codes would save a lot of time and money for the Election Commission. It is possible to do the same analysis using excel skills alone, however python codes written to audit this election results can be applied to audit any other election results on a local, state and even federal level elections.


* 1. Scalability: The screenshot of codes below demonstrates the usage of Python's Lists and Dictionaries to automatically assign Candidate's name, County name and votes cast for different candidates in different regions. The same method can be adopted in auditing any other elections with different candidate lists across different geographies.

    ![Resources/Lists_and_Dictionaries.png](https://github.com/berniemanu/Election_Analysis/blob/8c0fa1d4c584dc7103ffaafa551c3cdfbad0cac8/Resources/Lists_and_Dictionaries.png)


* 2. Versatality: The screenshot of codes below demonstrates the usage of Python's for loop to automatically loop through large CSV files and count votes cast for each candidate and votes cast in different counties. The same method can be adopted in counting votes in any other elections.

    ![Resources/Automating_vote_counting.png](https://github.com/berniemanu/Election_Analysis/blob/8c0fa1d4c584dc7103ffaafa551c3cdfbad0cac8/Resources/Automating_vote_counting.png)


* 3. Elegant Report Generation: Python codes written to audit this election has generated simple yet effective outputs in both the terminal as well as the text file as pictured below.

    ![Resources/Election_results_in_Command_Line.png](https://github.com/berniemanu/Election_Analysis/blob/8c0fa1d4c584dc7103ffaafa551c3cdfbad0cac8/Resources/Election_results_in_Command_Line.png)


    ![Resources/Election_results_saved_in_Text_File.png](https://github.com/berniemanu/Election_Analysis/blob/8c0fa1d4c584dc7103ffaafa551c3cdfbad0cac8/Resources/Election_results_saved_in_Text_File.png)


