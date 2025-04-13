# Remove Non-Integers
# Complete the remove_nonints() function that takes a list and returns a new list with all the non-integer types removed.
# remove_nonints(["1", 1, "3", "400", 4, 500])
# Remaining list after removing nonints = [1, 4, 500] 

def remove_nonints(nums): 
    list_int = []
    
    for num in nums: 
        if type(num) == int:
            list_int.append(num) 

    return list_int