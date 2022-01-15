import sys
from math import sqrt
if len(sys.argv)==2:
    n=int(sys.argv[1])
    i=2
    premier=True
    while i<=sqrt(n) and premier==True:
        if not n%i:
            premier=False
        i=i+1

    if not premier:
        print(n,'est compose')
    else:
        print(n,'est premier')
else:
    print("Usage : estPremier.py nombre")
