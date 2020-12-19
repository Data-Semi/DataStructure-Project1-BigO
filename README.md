# DataStructure-Project1-BigO
This is the first project in Udacity's DataStructure Nano Degree.

# Investigating Texts and Calls
## Project Overview
In this project, I have completed five tasks based on a fabricated set of calls and texts exchanged during September 2016. I have used Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, I have performed run time analysis of my solution and determine its efficiency.

### About the data
The text and call data are provided in csv files.

The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

### About the code
In Tasks 3 and 4, you can use in-built methods sorted() or list.sort() for sorting which are the implementation of Timsort and Samplesort, respectively. Both these sorting methods have a worst-case time-complexity of O(n log n). Check the below links to learn more about these methods:

How to use the above methods - https://docs.python.org/3/howto/sorting.html
Complexity analysis of Timsort and Samplesort - http://svn.python.org/projects/python/trunk/Objects/listsort.txt

### About Calculating Big O
After I have completed my solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of my solution. Document this for each problem and include this in my project submission.

