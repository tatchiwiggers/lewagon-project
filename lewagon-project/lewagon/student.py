from datetime import date
root_path = "/home/tatchiwiggers/code/batch-1852/classes/lewagon-project"
import sys; sys.path
sys.path.append(root_path)


class Student:

    school = 'lewagon'

    def __init__(self, name, age): # instance variable
        self.name = name
        self.age = age


    def says(self, something):
        print(f'{self.name} says {something}')

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)
