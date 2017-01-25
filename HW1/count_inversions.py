# -----------------------------------------------------------------------------
# Name:         count_inversions
# Purpose:      
# 
# Author:       Fiona Ding
# Created:      8/27/16
# -----------------------------------------------------------------------------

def merge_and_count_split_inv(left, right):
    """
    Merge two subarrays, and count split inversions.

    Args:
        left (int list): left subarray
        right (int list): right subarray

    Returns:
        (merged array, # of inversions)
    """
    inversions = 0

    merged = list()

    l_n = len(left)
    r_n = len(right)

    l_idx = 0
    r_idx = 0
    while l_idx<len(left) and r_idx<len(right):
        if left[l_idx] <= right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1

            inversions += l_n - l_idx   # number of unsorted elements in left

    if l_idx < len(left):
        # left still has elements - add to merged
        merged.extend(left[l_idx:])
    elif r_idx < len(right):
        # right still has elements - add to merged
        merged.extend(right[r_idx:])

    return (merged, inversions)


def sort_and_count(arr):
    """
    Recursively sort and count inversions

    Args:
        arr:
        inv

    Returns:

    """
    # Base case: if arr has only one element, it's already sorted, and no inversions
    if len(arr)<=1:
        return (arr, 0)

    pivot_idx = len(arr)//2

    # Recursively: split arr in half and sort each subarray
    left, l_inv = sort_and_count(arr[:pivot_idx])
    right, r_inv = sort_and_count(arr[pivot_idx:])

    merged, split_inv = merge_and_count_split_inv(left, right)

    return merged, l_inv + r_inv + split_inv


def testing():
    """Testing"""
    arr = [1,4,6,5,2]
    res = sort_and_count(arr)
    print("Expecting 4: ", res)

    arr = [1,3,5,2,4,6]
    res = sort_and_count(arr)
    print("Expecting 3: ", res)

    A = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
    res = sort_and_count(A)
    print("Expecting 56: ", res)

    # Test Case - #2 - 50 numbers
    A = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33,
         43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32,
         46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
    res = sort_and_count(A)
    print("Expecting 590: ", res)

    # Test Case - #3 - 100 numbers
    A =  [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28,
          18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0,
          96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42,
          95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64,
          93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77,
          30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    res = sort_and_count(A)
    print("Expecting 2372: ", res)


def main():
    with open('IntegerArray.txt', 'r') as fh:
        data = [int(line.strip()) for line in fh]

    res = sort_and_count(data)
    print(res[1])

if __name__ == "__main__":
    main()