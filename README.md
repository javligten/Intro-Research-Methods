# Intro-Research-Methods

What:
The program (as stated in the de_count.py file) takes the wiki_rug.txt file as data and
counts the amount of times "de" occurs regardless of capitalization.

Why:
This repository is made to make the de_count.py program and the wiki_rug.txt text available
for people who want to count the occurrences of the word "de" in the RUG wikipedia page.
It could also be used by others who want to use a similar tool 
and want to use this as a blueprint for their program.

How:
After cloning this directory from Github, access it through your terminal
by using the following command:
```
cd Intro-Research-Methods

```

Then to use the de_count program type I use these commands in Python version 3.8.8:
```
python de_count.py

```

For explanations about what every line and its purpose is:
Please refer to the comments provided in the de_count.py file

Data pre-processing:
The data that is used to get wiki_rug.txt is from the Wikipedia page
of the RUG. 

url: https://nl.wikipedia.org/wiki/Rijksuniversiteit_Groningen

I downloaded a html version of the page on my laptop and converted it into a .txt file.
Therefore, this file is not able to be automatically updated 
when new information is added to the page.

System Output:
At first I didn't use the read() function, which is why my output first came out as 0.
The output without adding the capitalized version of "de" was 608.
After adding both capitalized and non-capitalized occurrences the output was 654.

System Variations:
I cloned my repository to VS (Visual Stusio Code). 
If you use another ocde editor, it could be that quotation marks are interpreted differently.