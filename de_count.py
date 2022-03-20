# File name: de_count.py
# Author: Jaylee van Ligten
# This program takes the data from rug.txt and
# counts the occurrences of the word "de"

# Opens the rug.txt file to enable it for reading.
file = open("wiki_rug.txt", "r")
# Takes data from the text file by 'reading' through it.
data = file.read()
# Counts the amount of lowercase and uppercase occurrences of "de" in the file.
occurrences_lower = data.count("de")
occurrences_upper  = data.count("De")
# Prints a statement including the total amount of times "de" occurs in the file.
print('The word "de" appears', occurrences_lower + occurrences_upper, 
'times in this file.')
