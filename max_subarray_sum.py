def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            s = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i
    return max_so_far, arr[start:end+1]


    
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Find the maximum subarray sum and its elements
max_sum, max_subarray = max_subarray_sum(arr)

# Output the maximum subarray sum and its elements
print("Maximum Subarray Sum:", max_sum)
print("Maximum Subarray:", max_subarray)