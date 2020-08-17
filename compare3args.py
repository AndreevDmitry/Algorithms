import sys

#1.1.3 Write a program that takes three integer command-line arguments 
# and prints equal if all three are equal, and not equal otherwise.

def compare3args(arg1, arg2, arg3):
    if (arg1 == arg2 and arg2 == arg3):
        print("Equal")
    else:
        print("Not equal")

compare3args(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[2]))