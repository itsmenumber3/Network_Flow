"""
COSC364-23S1 Internet Technology and Engineering - Network Flow Assignment

Takes a desired number of source, transit and destination nodes
and writes a lp file for cplex that will optimize load of all paths through
the transit nodes so that load is evenly distributed.

Created by: Jonathan Nicholas
"""
def createFile(X,Y,Z):
    #Open the file
    file = open("cplex_X{}_Y{}_Z{}.lp".format(X,Y,Z), "w+")

    file.write("Minimize\n")
    file.write("r\n")
    file.write("Subject to\n")

    # Demand value of paths between source and destination equal to sum of ij
    for x in range(1,X+1):
        for z in range(1,Z+1):
            for y in range(1,Y+1):
                if y != Y:
                    file.write("x{}{}{} + ".format(x,y,z))
                else:
                    file.write("x{}{}{} = {}\n".format(x,y,z,x+z))

    # Load utilisation across all transit routers
    for y in range (1,Y+1):
        for x in range(1, X+1):
            for z in range(1,Z+1):
                if (x != X) or (z != Z):
                    file.write("x{}{}{} + ".format(x,y,z))
                else:
                    file.write("x{}{}{} - r <= 0\n".format(x,y,z))

    # Capacity constraints for links between Source and Transit nodes
    for x in range(1, X+1):
        for y in range(1,Y+1):
            for z in range(1,Z+1):
                if z != Z:
                    file.write("x{}{}{} + ".format(x,y,z))
                else:
                    file.write("x{}{}{} - c{}{} = 0\n".format(x,y,z,x,y))

    # Capacity constraints for links between Transit and Destination nodes
    for y in range(1,Y+1):
        for z in range(1,Z+1):
            for x in range(1, X+1):
                if x != X:
                    file.write("x{}{}{} + ".format(x,y,z))
                else:
                    file.write("x{}{}{} - d{}{} = 0\n".format(x,y,z,y,z))

    # Equal demand across the paths between each Source and Destination node pair
    for x in range(1,X+1):
        for z in range(1,Z+1):
            for y in range(1, Y+1):
                file.write("2 x{}{}{} - ".format(x,y,z))
                file.write("{} u{}{}{} = 0\n".format(x+z,x,y,z))
                    
    # Maximum 2 paths between each Source and Destination node pair
    for x in range(1,X+1):
        for z in range(1,Z+1):
            for y in range(1,Y+1):
                if y != Y:
                    file.write("u{}{}{} + ".format(x,y,z))
                else:
                    file.write("u{}{}{} = 2\n".format(x,y,z))


    file.write("\nBounds \n")
    # Bounds for load utilization variable
    file.write("r >= 0")
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

    file.write("\nBinary \n")
    # Each indicator variable set as a binary number
    for x in range(1,X+1):
        for z in range(1,Z+1):
            for y in range(1,Y+1):
                file.write("u{}{}{}\n".format(x,y,z))

    file.write("end\n")


def main():
    # Get a positive X value
    while True:
        try:
            X = int(input("Enter a positive integer for the number of source nodes: "))
            if X > 0:
                break  # Valid positive integer entered, exit the loop
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    # Get a positive Y value
    while True:
        try:
            Y = int(input("Enter a positive integer for the number of transit nodes: "))
            if Y > 0:
                break  # Valid positive integer entered, exit the loop
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    # Get a positive Z value
    while True:
        try:
            Z = int(input("Enter a positive integer for the number of destination nodes: "))
            if Z > 0:
                break  # Valid positive integer entered, exit the loop
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Create the lp with the entered values
    createFile(X,Y,Z)

if __name__ == '__main__':
    main()