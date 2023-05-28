import sys
import random

y_series = [3,4,5,6,7]
X = 7
Y = y_series[random.randint(0,4)]
Z = 7

#For appendix (X=3, Y=2, Z=3)

if len(sys.argv) > 1:
    X = int(sys.argv[1])
    Y = int(sys.argv[2])
    Z = int(sys.argv[3])

file = open("cplex_X{}_Y{}_Z{}.lp".format(X,Y,Z), "w+")

print("X =", X)
print("Y =", Y)
print("Z =", Z)

file.write("Minimize 1\n")

file.write("Subject to\n")

# Demand value of paths equal to sum of ij as specified on page 3
for x in range(1,X+1):
    for z in range(1,Z+1):
        for y in range(1,Y+1):
            if y != Y:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} = {}\n".format(x,y,z,x+z))

# Capacity constraints
for x in range(1, X+1):
    for y in range(1, Y+1):
        for z in range(1,Z+1):
            if z != Z:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} - 100r = 0\n".format(x,y,z))

file.write("\nBounds \n")
# Bounds
for x in range(1, X+1):
    for y in range(1, Y+1):
        for z in range(1,Z+1):
            file.write("x{}{}{} >= 0\n".format(x,y,z))

file.write("r >= 0")

