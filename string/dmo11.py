course = 'Python for Beginners'
print(len(course))  # len() is a general function
upper = course.upper()
print(upper)

lower = course.lower()
print(lower)  # upper() & lower() are method. these are specific to Strings. functions associated with specific
# object/class are method.

print(course.find('t'))  # return a . //CASE SENSITIVE
print(course.find('O'))
print(course.find('Beginners'))  # //CASE SENSITIVE

print(course.replace('beginners', 'Absolute Beginners'))  # CASE SENSITIVE
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'Z'))  # CASE SENSITIVE

print(course)
print('Python' in course)  # #CASE SENSITIVE
