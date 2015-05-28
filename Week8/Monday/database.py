import sqlite3


class CreateDB:
    def __init__(self):
        self.db = sqlite3.connect('HackBGStudents')
        # gets the response of the query in dict format
        # instead of a list
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
            id INTEGER PRIMARY KEY,
            github TEXT,
            name TEXT) """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Courses(
            id INTEGER PRIMARY KEY,
            name TEXT) """)

        # primary key по желание
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Students_To_Courses(
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES Students(id),
            FOREIGN KEY(course_id) REFERENCES Courses(id)) """)

    def add_student(self, github, name, course_names):
        self.cursor.execute("""INSERT INTO Students(github, name)
                VALUES(?, ?)
            """, (github, name))
        self.db.commit()

        student_id = self.cursor.lastrowid
        self.cursor.lastrowid

        for course in course_names:
            self.cursor.execute("""SELECT id FROM Courses
                                    WHERE Courses.name = (?)""", (course, ))
            course_ids = self.cursor.fetchall()
            for course_id in course_ids:
                self.cursor.execute("""INSERT INTO
                    Students_To_Courses(student_id, course_id)
                    VALUES(?, ?)
                    """, (student_id, course_id[0]))
        self.db.commit()

    def list_students(self):
        return self.cursor.execute("""SELECT id, github, name
            FROM Students
            """)

    def delete_student(self, student_id):
        self.cursor.execute("""DELETE FROM Students
            WHERE id = (?)
            """, (student_id, ))
        self.db.commit()

    def add_course(self, name):
        self.cursor.execute("""INSERT INTO Courses(name)
            VALUES(?)
            """, (name, ))
        self.db.commit()

    def list_courses(self):
        return self.cursor.execute("""SELECT id, name
            FROM Courses
            """)

    def delete_course(self, course_id):
        self.cursor.execute("""DELETE FROM Students
            WHERE id = (?)
            """, (course_id, ))
        self.db.commit()

    def students_courses(self, student_id):
        return self.cursor.execute("""SELECT *
                               FROM Students_To_Courses
                               JOIN Courses
                               ON Students_To_Courses.student_id = (?)
                               AND
                               Students_To_Courses.course_id = Courses.id""",
                                   (student_id, ))
