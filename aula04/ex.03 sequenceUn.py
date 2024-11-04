"""
This program generates 20 terms of a sequence by a recurrence relation.
Change it to show all positive terms of the sequence and count them.
Format the columns to make the output look like this:
   n        Un
   0   100.000
   1    99.990
   2    99.980
"""

print("n", "Un")
Un = 100
n=0
while Un > 0: 
   print(n, Un)                  # Un = each term of the sequence. Initially = U0
   Un = 1.01*Un - 1.01   
   n+= 1