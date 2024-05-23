def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:

        max_rest = find_max(arr[1:])

        if arr[0] > max_rest:
            return arr[0]
        else:
            return max_rest
arr = [1,2,3,5,9]

print("Maximum number in the list:", find_max(arr))