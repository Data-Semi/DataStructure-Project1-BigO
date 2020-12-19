"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


time_number_dict = {}  # number: time ditionary for prepare furthure process

for num1, num2, time, duration in calls:  # Big O: O(2n)
    if num1 in time_number_dict:
        time_number_dict[num1] += float(duration)
    else:
        time_number_dict[num1] = float(duration)

    if num2 in time_number_dict:
        time_number_dict[num2] += float(duration)
    else:
        time_number_dict[num2] = float(duration)

max_kv = max(time_number_dict.items(), key=lambda x: x[1])  # Big O: O(2n)
print("{} spent the longest time, {} seconds,\
 on the phone during September 2016."
      .format(max_kv[0], max_kv[1]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time,
 <total time> seconds, on the phone during
September 2016.".
"""
