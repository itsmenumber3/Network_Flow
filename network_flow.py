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

file.write("Minimize\n")

file.write("Subject to\n")

file.write("\|DEM| For all Sx and Dz = hxz (= x+z)\n")
# Demand value of paths equal to sum of ij as specified on page 3
for x in range(1,X+1):
    for z in range(1,Z+1):
        for y in range(1,Y+1):
            if y != Y:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} = {}\n".format(x,y,z,x+z))
"""
# Capacity constraints as per exmaple (dont think apply to assignment)
for x in range(1, X+1):
    for y in range(1, Y+1):
        for z in range(1,Z+1):
            if z != Z:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} - 100 r = 0\n".format(x,y,z))
"""
file.write("\|CAP| For all Sx and Ty = cxy\n")
for x in range(1, X+1):
    for y in range(1,Y+1):
        for z in range(1,Z+1):
            if z != Z:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} = c{}{}\n".format(x,y,z,x,y))


file.write("\|CAP| For all Ty and Dz = dyz\n")
for y in range(1,Y+1):
    for z in range(1,Z+1):
        for x in range(1, X+1):
            if x != X:
                file.write("x{}{}{} + ".format(x,y,z))
            else:
                file.write("x{}{}{} = d{}{}\n".format(x,y,z,y,z))


file.write("\|CAP| For all Sx and Dz = hxz(for all uxyz)\n")
for x in range(1,X+1):
    for z in range(1,Z+1):
        for y in range(1, Y+1):
            if y != Y:
                file.write("2 x{}{}{} + ".format(x,y,z))
            else:
                file.write("2 x{}{}{} = ".format(x,y,z))
                
        for y in range(1,Y+1):
            if y != Y:
                file.write("{} u{}{}{} + ".format(x+z,x,y,z))
            else:
                file.write("{} u{}{}{}\n".format(x+z,x,y,z))

file.write("\Two distinct paths\n")
for x in range(1,X+1):
    for z in range(1,Z+1):
        for y in range(1,Y+1):
            if y != Y:
                file.write("u{}{}{} + ".format(x,y,z))
            else:
                file.write("u{}{}{} = 2\n".format(x,y,z))


file.write("\nBounds \n")
# Bounds for decision variables
for x in range(1, X+1):
    for y in range(1, Y+1):
        for z in range(1,Z+1):
            file.write("x{}{}{} >= 0\n".format(x,y,z))

#Bounds for capacity variables
#Source to Transit link
for x in range(1,X+1):
    for y in range(1, Y+1):
        file.write("c{}{} >= 0\n".format(x,y))

#Transit to Destination link
for y in range(1,Y+1):
    for z in range(1,Z+1):
        file.write("d{}{} >= 0\n".format(y,z))

#Uxyz not required to be in bounds as automatically assumed as binary if not initialised
#file.write("r >= 0")


file.write("end\n")

