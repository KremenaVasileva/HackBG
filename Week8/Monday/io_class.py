from database import CreateDB
from json_crawler import JSONCrawler


class IO:
    @staticmethod
    def init_database(database):
        my_database = CreateDB()
        crawler = JSONCrawler()

        all_courses = crawler.get_all_courses()
        all_students = crawler.get_students()

        for course in all_courses:
            my_database.add_course(course)

        for student in all_students:
            # student[0] is the github
            # student[1] is the student's name
            # all_students - list of tuples
            student_courses = crawler.get_courses_for_student(student[0], student[1])
            my_database.add_student(student[0], student[1], student_courses)

    @staticmethod
    def list_students(database):
        students = database.list_students()
        for student in students:
            print("{} - {}".format(student['name'], student['github']))

    @staticmethod
    def list_courses(database):
        courses = database.list_courses()
        for course in courses:
            print("{}".format(course['name']))

    @staticmethod
    def courses_for_all_students(database):
        all_students = database.list_students()
        student_ids = []
        for student in all_students:
            student_ids.append(student['id'])

        for student_id in student_ids:
            pass

    @staticmethod
    def execute_command(database, user_input):
        all_commands = {
                        "students": IO.list_students,
                        "courses": IO.list_courses,
        }
        try:
            all_commands[user_input](database)
        except:
            print("Invalid command!")
