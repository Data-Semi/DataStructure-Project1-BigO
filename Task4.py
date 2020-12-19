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

calls_num = set()  # numbers which made calls
calls_recive_num = set()  # numbers which received calls
texts_total_num = set()  # numbers which sent or received texts

for call in calls:
    calls_num.add(call[0])
    calls_recive_num.add(call[1])

for text in texts:
    texts_total_num.add(text[0])
    texts_total_num.add(text[1])

# The asswer should be calls_num - calls_recive_num - texts_total_num
tele_num = calls_num.difference(calls_recive_num)  # Big O: O(n)
tele_num = tele_num.difference(texts_total_num)  # Big O: O(n)

# to make in lexicographic order, change type to list type
tele_num_sorted = list(tele_num)  # Big O: O(n)
tele_num_sorted.sort()  # Big O: O(nlogn)

print("These numbers could be telemarketers: ")
print(*tele_num_sorted, sep="\n")


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per
line in lexicographic order with no duplicates.
"""
