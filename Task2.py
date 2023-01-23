from typing import List

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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def task2(texts: List, calls: List) -> None:
    dic = {}
    for idx, v in enumerate(calls):
        caller = v[0]
        callee = v[1]
        duration = int(v[3])
        if caller in dic:
            dic[caller] += duration
        else:
            dic[caller] = duration

        if callee in dic:
            dic[callee] += duration
        else:
            dic[callee] = duration

    max_value = 0
    max_caller = None
    for p in dic:
        if dic[p] > max_value:
            max_value = dic[p]
            max_caller = p

    print(f"{max_caller} spent the longest time, {max_value} seconds, on the phone during September 2016")

"""
Big o should be O(n) as the program has to loop through each line of the input(although loop twice) to calc telephone durations, 2n -> O(n)
"""

if __name__ == "__main__":
    task2(texts, calls)
