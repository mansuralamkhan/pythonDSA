def lis(arr):
    n = len(arr)

    dp = [1] * n
    lis_sequence = []

    for i in range (1, n):
        for j in range (i):
            if arr[i]> arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_lenth = max(dp)

    current_lenth = max_lenth
    for i in range(n-1, -1, -1):
        if dp[i] == current_lenth:
            lis_sequence.insert(0, arr[i])
            current_lenth -= 1
    return max_lenth , lis_sequence

arr = list(map(int, input("Enter the elements of the array seperated by space: ").split()))

lis_length, lis_elements = lis(arr)


print("Length of longest Increasing sequence: ", lis_length)
print("Longest Increaseing Subsequence", lis_elements)