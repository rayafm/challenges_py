# Assignment
# Complete the average_followers function. 
# It should return the average of the given list of numbers.

def average_followers(nums):
    sum = 0
    if len(nums) == 0:
        return None
    else:
        for num in nums:
            sum += num 

    return sum / len(nums)