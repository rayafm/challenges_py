# Assignment
# Complete the median_followers() function to find the median follower count of the given list of numbers.

# Order matters - You'll probably want to use the sorted() function to help you out. 
# Be sure to appropriately handle lists of even length.

def median_followers(nums):
    sorted_nums = sorted(nums) 
    median = 0
    seq_med = len(nums) // 2

    if len(nums) == 0:
        return None
    elif len(nums) % 2 == 0:
        median += (sorted_nums[seq_med-1] + sorted_nums[seq_med]) / 2
    else:
        median += sorted_nums[seq_med]

    return median