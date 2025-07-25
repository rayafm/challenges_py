# FizzBuzz 
# Complete the fizzbuzz function that loops over all the numbers 
# from start to end (excluding the end value) and adds them to a list it returns. 
# If the number is a multiple of 3, instead of appending the number, append "fizz". 
# If the number is a multiple of 5, instead append "buzz". 
# If it is a multiple of 3 and 5 then instead append "fizzbuzz".
# For example, if start = 1 and end = 8, then the resulting list would contain: 
# [
#   1,
#   2,
#   "fizz",
#   4,
#   "buzz",
#   "fizz",
#   7,
# ] 

def fizzbuzz(start, end):
    list_fzbz = []
    
    for num in range(start, end):
       if num % 3 == 0 and num % 5 == 0:
           list_fzbz.append("fizzbuzz") 
       elif num % 3 == 0:
           list_fzbz.append("fizz") 
       elif num % 5 == 0:
           list_fzbz.append("buzz") 
       else: 
           list_fzbz.append(num) 

    return list_fzbz