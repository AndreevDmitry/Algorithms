"""
Selection sort implementation
Example:$ python3 selection_sort.py 3,2,4,1
[1, 2, 3, 4]
"""

import sys

def find_smallest(array):
    """
    Find smallest value from passed array
    """
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    """
    Execute selection sort of passed array.
    Returns sorted array from smallest or
    None if array not exists
    """
    new_array = []
    for _ in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


print(selection_sort(list(map(int, sys.argv[1].split(',')))))

def test():
    """Some tests"""
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([0]) == [0]
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert selection_sort([0, -1, 1]) == [-1, 0, 1]
    print("-----------------Tests are PASSED-----------------------")

if __name__ == "__main__":
    test()
