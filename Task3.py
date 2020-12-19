"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Part A:
# just add 080
# if start with 7,8,9
#  take the first 4 digits
# add 140

# ----psudo code---------
# if num1 start with (080):
#   count call_total += 1
#     if num2 start with (080):
#       count call_B += 1
# call_B/call_total


code_list = {"(080)"}  # list of area code, for Part A
# Because (080) is the area code for fixed line telephones in Bangalore.
call_total = 0  # count of (080)... made calls
call_B = 0  # count of (080)... calls an other (080)...

for num1, num2, time, duration in calls:  # Big O: O(2n)
    if num1[:5] == "(080)":  # called from (080)*
        call_total += 1
        if num2[:5] == "(080)":  # called to another (080)*
            call_B += 1
        elif num2[0] in ["7", "8", "9"]:  # Check prefix of a mobile number
            code_list.add(num2[:4])
        elif num2[:3] in ["140"]:  # Check calls from Telemarketers.
            code_list.add(num2[:3])
        elif num2.startswith('('):
            code_list.add(num2[:num2.find(')') + 1])

# delete duplication in list, and sort by lexicographic order
code_list_no_dup = list(code_list)  # Big O: O(2n)
code_list_no_dup.sort()  # Big O: O(nlogn)
print("The numbers called by people in Bangalore have codes:")
print(*code_list_no_dup, sep="\n")

percentage = (call_B / call_total) * 100
print("{:.2f} percent of calls from fixed lines in Bangalore\
 are calls to other fixed lines in Bangalore.".format(percentage))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line
in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
