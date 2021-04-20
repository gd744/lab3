"""
create a list to store 5 numbers(floats)
capture user's inputs 5 times for grades
eacc h time we capture the user's input, we append the number to the list
sort the list asscending, then splice the items starting at index 2
once we have three highest numbers in the list, we sum them up and divide by 3
output a message to the user
end
"""
"""
PSUEDOCODE

create list
 capture input
 append number to list

 capture input
 append nmumber to list

 capture input
 append number to list

  capture input
 append number to list

  capture input
 append number to list

  capture input
 append number to list

 print message to user
"""


grades = []

grade = input( "Enter the first grade: ")
grades.append(float(grade))

grade = input( "Enter the second grade: ")
grades.append(float(grade))

grade = input( "Enter the third grade: ")
grades.append(float(grade))

grade = input( "Enter the fourth grade: ")
grades.append(float(grade))

grade = input( "Enter the fifth grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades / 3

print("Average Grades {0:2f}%".format(result))