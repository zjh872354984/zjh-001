#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])
except:
    print("Parameter Error")

tax0 = salary - 3500
if tax0<=0:
    tax0 = 0
    tax = 0
elif tax0<=1500:
    tax = tax0 * 3/100 - 0
elif tax0<=4500:
    tax = tax0 * 10/100 - 105
elif tax0<=9000:
    tax = tax0 * 20/100 - 555
elif tax0<=35000:
    tax = tax0 * 25/100 - 1005
elif tax0<=55000:
    tax = tax0 * 30/100 - 2755
elif tan0<=80000:
    tax = tax0 * 35/100 - 5505
else:
    tax = tax0 * 45/100 - 13505
print(format(tax,".2f"))
