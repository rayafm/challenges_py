# Pupil Records
# Players can recruit wizard pupils into their armies. 
# Depending on the pupil's marks, they gain different in-game abilities.

# Assignment
# Complete the Student class.

# Complete the constructor:
# Set the name parameter to the name instance variable.
# Initialize a private data member called __courses to an empty dictionary.
# Create the calculate_letter_grade method that takes a score parameter:
# If score is 90 or above the function should return "A"
# If score is between 80 and 89 (inclusive) the function should return "B"
# If score is between 70 and 79 (inclusive) the function should return "C"
# If score is between 60 and 69 (inclusive) the function should return "D"
# Otherwise, the function should return "F"
# Create the add_course method that takes course_name and score parameters:
# Calculate letter grade based on the score.
# Set the course_name as a key in the courses dictionary 
# and the calculated letter grade as the corresponding value.
# Create the get_courses method, which returns the private __courses dictionary.

class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score>=90:
            return "A"
        elif score>=80 and score<=89:
            return "B"
        elif score>=70 and score<= 79:
            return "C"
        elif score>=60 and score<=69:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        res = self.calculate_letter_grade(score)
        self.__courses[course_name] = res

    def get_courses(self):
        return self.__courses