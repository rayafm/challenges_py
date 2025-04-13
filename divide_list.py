# List Division
# Write a function called divide_list() that takes a list and a number as input. 
# The function returns a new list that contains all the elements of the original list 
# except they have been divided by the second input. 

# divided_list = divide_list([6, 8, 10], 2)
# print(divided_list) # [3.0, 4.0, 5.0]

def divide_list(nums, divisor):
    divided_list = [num / divisor for num in nums] 

    return divided_list