"""
1.1.3 Write a program that takes three integer command-line arguments
and prints equal if all three are equal, and not equal otherwise.
"""

import sys

def compare3args(arg1, arg2, arg3):
    """Return "Equal" if all 3 args are equal, otherwise "Not Equal" """
    if (arg1 == arg2 and arg2 == arg3):
        print(arg1, ",", arg2, "and", arg3, "are equal")
        return True

    print(arg1, ",", arg2, "and", arg3, "are not equal")
    return False

compare3args(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

def test():
    """Some tests"""
    print("---------------Run tests--------------------")
    assert compare3args("1", "1", "1") is True
    assert compare3args("1.0", "1", '1') is False
    assert compare3args("1", "2", "1") is False
    assert compare3args("-1", "-1", "-1") is True
    assert compare3args("1", "2", "3") is False
    assert compare3args(55, "55", "55") is False

if __name__ == "__main__":
    test()
