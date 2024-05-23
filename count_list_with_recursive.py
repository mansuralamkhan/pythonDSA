def count_items(arr):

    if not arr:
        return 0
    else:
        return 1 + count_items(arr[1:])
    

arr = [1,2,3,4,5,6,9]
print("Number of items in the list:", count_items(arr))