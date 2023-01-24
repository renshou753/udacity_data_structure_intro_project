from typing import List

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
def task3_a(texts: List, calls: List) -> None:
    # find calls initiated from area code 080
    l = [x for x in calls if x[0].startswith("(080)")]

    codes = []
    for call in l:
        if "(" in call[1]:
            code = re.search('\(([^)]+)', call[1]).group(1)
            codes.append(code)
        elif " " in call[1]:
            code = call[1][:4]
            codes.append(code)
        elif call[1].startswith("140"):
            codes.append("140")

    result = sorted(set(codes))
    
    print(f"The number called by people in Bangalore have codes:")
    for x in result:
        print(x)

"""

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def task3_b(texts: List, calls: List) -> None:
    l1 = [x for x in calls if x[0].startswith("(080)")]
    l2 = [x for x in l1 if x[1].startswith("(080)")]

    per = round(len(l2)/len(l1) * 100, 2)
    print(f"{per} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore")

"""
Big o for part A should be nlog(n), the program first needs to loop through each line of the input to get corresponding area code, time complexity for this step should be O(n); later the program needs to sort the list which has time complexity of nlog(n); since nlog(n) is more consuming then n here I would choose O(nlog(n)) 

Big o for part B should be 2n, approximately to O(n) because the program needs to loop through each line of the input roughly twice
"""

if __name__ == "__main__":
    task3_a(texts, calls)
    task3_b(texts, calls)
