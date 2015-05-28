import requests
from student import Student


class JSONCrawler:
    def __init__(self):
        self.all_data = requests.get("https://hackbulgaria.com/api/students/").json()
        self.all_students = []
        self.courses_names = set()

    def get_students(self):
        for student in self.all_data:
            student_name = student['name']
            student_github = student['github']
            self.all_students.append((student_github, student_name), )
        return self.all_students

    def get_all_courses(self):
        for student in self.all_data:
            for course in student['courses']:
                self.courses_names.add(course['name'])
        return self.courses_names

    def get_courses_for_student(self, github, name):
        student_courses = []
        for student in self.all_data:
            if student['name'] == name and student['github'] == github:
                for course in student['courses']:
                    student_courses.append(course['name'])
        return student_courses


# crawler = JSONCrawler()
# print(crawler.get_all_courses())
# print(crawler.get_courses_for_student("https://github.com/tonynho", "Антон Петков"))
