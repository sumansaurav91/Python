
employee_file = open("employee.txt", "a")
print(employee_file.writable())
employee_file.write("\nSaurav - Python Data structure Instructor")
employee_file = open("employee.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("index.html", "w")
employee_file.write("<p>Hello World!</p>")
employee_file.close()