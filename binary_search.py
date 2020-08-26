"""
Binary search implementation
Example:$ python3 binary_search.py 1 1,2,3,4
0
"""

import sys

def binary_search(item, array):
    """
    Execute binary search of passed item
    in passed array. Returns position of item or
    None if not exists
    """
    high = len(array) - 1
    low = 0
    while low <= high:
        mid = int((low + high)/2)
        guess = array[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid

    return None

print(binary_search(int(sys.argv[1]), list(map(int, sys.argv[2].split(',')))))

def test():
    """Some tests"""
    assert binary_search(1, [1, 2, 3, 4]) == 0
    assert binary_search(0, [0]) == 0
    assert binary_search(4, [1, 2, 3, 4]) == 3
    assert binary_search(5, [1, 2, 3, 4]) is None
    assert binary_search(0, [-1, 0, 1]) == 1
    print("-----------------Tests are PASSED-----------------------")

if __name__ == "__main__":
    test()
