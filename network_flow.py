import sys
import random

y_series = [3,4,5,6,7]
X = 7
Y = y_series[random.randint(0,4)]
Z = 7

#For appendix (X=3, Y=2, Z=3)

if len(sys.argv) > 1:
    X = sys.argv[1]
    Y = sys.argv[2]
    Z = sys.argv[3]


print("X =", X)
print("Y =", Y)
print("Z =", Z)


