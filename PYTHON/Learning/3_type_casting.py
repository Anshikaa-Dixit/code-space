# Typecasting is the process of converting a datatype into another datatype(str(),int(),float(),bool())

name = "Anshika"
n = ""
age = 20
cgpa = 8.7
is_student = True

print(type(name))
print(type(n))
print(type(age))
print(type(cgpa))
print(type(is_student))

age = str(age)
cgpa = int(cgpa)
is_student = float(is_student)
name = bool(name)
n = bool(n)

print(age)
print(cgpa)
print(is_student)
print(name)
print(n)