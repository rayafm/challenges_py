# Logarithmic Scale
# In some cases, data can span several orders of magnitude, 
# making it difficult to visualize on a linear scale. 
# A logarithmic scale can help by compressing the data so that it's easier to understand.

# For example, at LockedIn we have influencers with follower counts ranging from 1 to 1,000,000,000. 
# If we want to plot the follower count of each influencer on a graph, 
# it would be difficult to see the differences between the smaller follower counts. 
# We can use a logarithmic scale to compress the data so that it's easier to visualize.

# Assignment
# Write a function log_scale(data, base) that takes a list of positive numbers data, 
# and a logarithmic base, and returns a new list with the logarithm of each number in the original list, 
# using the given base.

# You may want to use the math.log() function. 

import math 

def log_scale(data, base):
    res_list = []

    for num in data:
        res = math.log(num, base)

        res_list.append(res)

    return res_list