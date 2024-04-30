import json


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def read_json(self):
        with open("students.json", "r") as json_file:
            self.scores = json.load(json_file)

    def calc_average(self):
        averages = {}
        for student in self.scores["students"]:
            name = student["name"]
            grades = student["grades"]
            average = sum(grades) / len(grades)
            averages[name] = average
        return averages

    def write_json(self):
        with open("output.json", "w") as json_file:
            json.dump(self.calc_average(), json_file)


student = Student("", 0, [])
student.read_json()
student.write_json()

