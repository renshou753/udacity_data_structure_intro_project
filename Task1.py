from typing import List

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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def task1(texts: List, calls: List) -> None:
    l = set([x[0] for x in texts] + [x[1] for x in texts] + [x[0] for x in calls] + [x[1] for x in calls])
    print(f"There are {len(l)} different telephne numbers in the records")

"""
Big o should be O(n) as the program has to scan through each line of the input to get telephone numbers
"""

if __name__ == "__main__":
    task1(texts, calls)
