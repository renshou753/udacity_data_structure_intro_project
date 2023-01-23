"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

from typing import List

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


"""
Big o for this problem should be O(1), program just tried to find the first and last lines from the input, irrespective of the input size
"""
def task0(texts: List, calls: List) -> None:
    print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time") 
    print(f"Last record of calls, {calls[-1][0]} texts {calls[-1][1]} at time, lasting {calls[-1][3]} seconds")

if __name__ == "__main__":
    task0(texts, calls)
