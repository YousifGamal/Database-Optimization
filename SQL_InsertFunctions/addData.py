import sys
import os
from connect import ConnectMySQL
sys.path.append(os.path.abspath('../SQL_InsertFunctions'))
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from randomData import *
from NoSQL_InsertFunctions.connect import *
import NoSQL_InsertFunctions.addData as NoSQL
connectDB = ConnectMySQL()
cursorDB = connectDB.cursor()
'''
    Students Queries
'''


def insertStudent(items, oneOrMany):
    sql = "INSERT INTO `student`(`student_id`, `first_name`, `last_name`, `year`) VALUES (%s,%s,%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showStudents():
    cursorDB.execute("SELECT * FROM `student`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Instructor Queries
'''


def insertInstructor(items, oneOrMany):
    sql = "INSERT INTO `instructor`(`instructor_id`, `first_name`, `last_name`, `degree`) VALUES (%s,%s,%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showInstructors():
    cursorDB.execute("SELECT * FROM `instructor`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Course Queries
'''


def insertCourse(items, oneOrMany):
    sql = "INSERT INTO `course`(`course_id`, `title`) VALUES (%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showCourses():
    cursorDB.execute("SELECT * FROM `course`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Lesson Queries
'''


def insertLesson(items, oneOrMany):
    sql = "INSERT INTO `lesson`(`lesson_id`, `title`) VALUES (%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showLessons():
    cursorDB.execute("SELECT * FROM `lesson`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Contains Queries
'''


def insertContain(items, oneOrMany):
    sql = "INSERT INTO `contains`(`course_id`, `lesson_id`) VALUES (%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showContains():
    cursorDB.execute("SELECT * FROM `contains`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Learns Queries
'''


def insertLearn(items, oneOrMany):
    sql = "INSERT INTO `learns`(`student_id`, `course_id`) VALUES (%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showLearns():
    cursorDB.execute("SELECT * FROM `learns`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


'''
    Teachs Queries
'''


def insertTeach(items, oneOrMany):
    sql = "INSERT INTO `teaches`(`instructor_id`, `course_id`) VALUES (%s,%s)"

    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql, values)
    else:
        cursorDB.executemany(sql, values)


def showTeachs():
    cursorDB.execute("SELECT * FROM `teaches`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)


def insertQueries(instructorNum, studentNum, courseNum):
    '''
        fill the course,lesson,contain tables
    '''
    coursesArray = []  # array that hold courses object

    for courseID in range(1, courseNum+1):
        title, lessonTitles, lessonIDs = course(courseID)
        lessons = []
        contains = []

        lessonsArr = []
        for i in range(0, len(lessonTitles)):
            lessons.append((lessonIDs[i], lessonTitles[i]))
            contains.append((courseID, lessonIDs[i]))

            lessonsArr.append(
                {"lessonId": lessonIDs[i], "title": lessonTitles[i]})

        insertCourse((courseID, title), 0)
        insertLesson(lessons, 1)
        insertContain(contains, 1)

        entry = [courseID, title, lessonsArr]
        coursesArray.append(entry)

    NoSQL.insertCourse(coursesArray, oneOrMany=1)

    '''
        fill the student,learn table
    '''

    usersArray = []  # array that hold users object

    for studID in range(1, studentNum+1):
        fname, lname, year = student()
        insertStudent((studID, fname, lname, year), 0)
        learn = []
        coursesRange = studentCourse()

        courses = []
        for courseID in coursesRange:
            learn.append((studID, courseID))
            courses.append({"courseId": courseID})
        insertLearn(learn, 1)

        usersArray.append([studID, fname, lname, 0, "", year, courses])
    NoSQL.insertUser(usersArray, oneOrMany=1)

    '''
        fill the instructor,teach table
    '''
    usersArray = []  # array that hold users object
    for instructorID in range(1, instructorNum+1):
        fname, lname, degree = instructor()
        insertInstructor((instructorID, fname, lname, degree), 0)
        teach = []
        coursesRange = instructorCourse()

        courses = []
        for courseID in coursesRange:
            teach.append((instructorID, courseID))
            courses.append({"courseId": courseID})
        insertTeach(teach, 1)

        usersArray.append([instructorID, fname, lname, 1, degree, "", courses])

    NoSQL.insertUser(usersArray, oneOrMany=1)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()


#insertQueries(10, 50, 40)
insertQueries(100, 40000, 40)