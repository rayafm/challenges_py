# Join Strings
# Write a function called join_strings() that takes a list of strings and returns a single string. 
# Concatenate the strings from the list end-to-end, in order, with a comma between them. 
# Don't use the .join() string method. 

# Example: 
# string_list = ["hello", "my", "friend"]
# joined_string = join_strings(string_list)
# print(joined_string) # "hello,my,friend" 

def join_strings(strings): 
    joined_str = "" 
    end_str = ""
    final_joined_str = "" 
    
    for i in range(0, len(strings)): 
        if i == len(strings)-1: 
            end_str = strings[i] 
        else:
            joined_str += strings[i] + "," 

    final_joined_str += joined_str + end_str

    return final_joined_str