# dna-matching

## About
This was a project I worked on as a part of a problem set provided in the CS50 course Harvard provides online.
A full description of the problem set can be found at https://cs50.harvard.edu/college/2020/spring/psets/6/dna/. 

## Purpose
The purpose of this project was to take a long series of text representing DNA evidence and iterate through the file 
to count the maximum number of times various strings are repeated consecutively. That data is then stored to memory and
compared vs. a list of possible suspects in a csv file to determine if there are any DNA matches.

## Testing
To run this program, enter the name of the csv file followed by the name of the .txt document you would like to compare
in the command line. A few examples of both documents have been provided in this project's assets. They answer key 
for each file is as follows:

*python dna.py assets/large.csv assets/11.txt* should result in 'Hermione'

*python dna.py assets/large.csv assets/15.txt* should result in 'Sirius'

*python dna.py assets/large.csv assets/16.txt* should result in 'No match'

*python dna.py assets/large.csv assets/17.txt* should result in 'Harry'