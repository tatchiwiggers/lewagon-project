from student import Student
from data_student import DataStudent

banana = Student('tatchi', 43)
print(banana.name)
print(banana.age)
print(banana.name, banana.age)
print(f'{banana.name} is {banana.age}!')
print(banana.school)

banana.says('Hi') # instance object
arnav = Student.from_birth_year('Arnav', 1963) # class object
print(arnav.age) # instance attribute
arnav.says(f'Heeeyyyyy, that is not right, I am younger than {banana.name}') # instance method

cam = DataStudent('Cam', 67, 1852)
print(cam.__dict__)
