# Minimum Number in Python

# Write a function called find_min() that finds the smallest number in a list
# find_min([1, 3, -1, 2]) -> -1
# find_min([18, 3, 7, 2]) -> 2

def find_min(nums): 
    min = nums[0]
    
    for i in range(0, len(nums)): 
        if nums[i] < min:
            min = nums[i]
    
    return min