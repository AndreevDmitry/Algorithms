"""
Binary search implementation
"""

import sys

def binary_search(start_value, end_value, item):
    """
    Creates sorted array and execute binary search
    of passed item. Retuns position of item or
    None if not exists
    """
    array_list = list(range(start_value, end_value+1))
    high = len(array_list) - 1
    low = 0
    while low <= high:
        mid = int((low + high)/2)
        guess = array_list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid

    return None

print(binary_search(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))

def test():
    """Some tests"""
    assert binary_search(1, 5, 1) == 0
    assert binary_search(0, 0, 0) == 0
    assert binary_search(-100, 100, 100) == 200
    assert binary_search(-100, 100, 300) is None
    assert binary_search(-1, 1, 0) == 1
    print("-----------------Tests are PASSED-----------------------")

if __name__ == "__main__":
    test()
