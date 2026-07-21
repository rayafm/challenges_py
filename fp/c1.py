# Toggle Case
# We need to add a feature to Doc2Doc that switches the capitalization of all the words in a line.

# Assignment
# Complete the toggle_case function using string methods. It takes a string as input line, and returns a string.

# If line is in titlecase, convert it to all uppercase and add three "!" to the end.
# If line is all uppercase, convert it to all lowercase except for the first letter and remove all trailing "!".
# If line is all lowercase or only the first letter is capitalized, convert it to title case.
# Otherwise, just return line unchanged. 

def toggle_case(line):
    if line.istitle():
        line_cv = line.upper() + "!!!"
        return line_cv
    if line.isupper():
        line_cv = line.capitalize().replace("!", "")
        return line_cv
    if len(line) > 0 and line[1:].islower():
        line_cv = line.title()
        return line_cv
        
    return line