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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def task4(texts:List, calls:List) -> None:
    # get all the phones that either send texts, receive texts or receive incoming calls
    l1 = set([x[0] for x in texts] + [x[1] for x in texts] + [x[1] for x in calls])

    marketers = []
    for call in calls:
        if call[0] not in l1 and call[0] not in marketers:
            marketers.append(call[0])

    result = sorted(set(marketers))

    print(f"These numbers could be telemarketers:")
    for x in result:
        print(x)
"""
Big o should be nlog(n), the program first needs to loop through each line of the input go get phone list, in my program looped roughly 4 times, time complexity for this step should be 4n -> O(n); later the program needs to sort the list which has time complexity of nlog(n); since nlog(n) is more time consuming I would choose O(nlog(n)) 
"""
    

if __name__ == "__main__":
    task4(texts, calls)

