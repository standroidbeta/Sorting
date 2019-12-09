# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             
        # TO-DO: swap
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # List iteration
    make_swap = True
    while make_swap:
        make_swap = False
        for i in range(0, len(arr) - 1):
            # Swap if right hand side neighbor is greater
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                make_swap = True

    return arr


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):
#
#
#     return arr