course = "Python programming fundamentals"
print(len(course));

print(course.upper())
print(course.lower())
print(course.title())

course = "    Python Programming Fundamentals    "
print(course.strip())
print(course.lstrip())
print(course.rstrip())

print(course.find("Pro"))
print(course.replace("Fundamentals", "Advanced"))

print("Python" in course)
print("python" in course)

