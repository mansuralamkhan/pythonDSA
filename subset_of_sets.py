def subsets(num):
    def backtracks(start, path):
        subsets.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtracks(i+1, path)
            path.pop()
    
    subsets = []
    backtracks(0, [])
    return subsets

nums = [1,2,3,4]
print("Subset of ", nums, ":", subsets(nums))