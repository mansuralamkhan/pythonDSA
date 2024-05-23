def recursive_sum(arr):

    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])
    
arr = [1,2,3,4,5]

print("Sum of array", recursive_sum(arr))