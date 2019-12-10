# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    while len(arrA) and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))

    if len(arrA) == 0:
        merged_arr = merged_arr + arrB
    else:
        merged_arr = merged_arr + arrA

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    ls, rs = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(ls, rs)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
