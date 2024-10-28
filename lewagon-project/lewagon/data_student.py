from student import Student

class DataStudent(Student):
    course = 'data science'

    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch
