import sys,os
from connect import Connect
sys.path.append(os.path.abspath('../SQL_InsertFunctions'))
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from randomData import *

'''
    Students Queries
'''
def insertStudent(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `student`(`student_id`, `first_name`, `last_name`, `year`) VALUES (%s,%s,%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showStudents(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `student`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()

'''
    Instructor Queries
'''
def insertInstructor(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `instructor`(`instructor_id`, `first_name`, `last_name`, `degree`) VALUES (%s,%s,%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showInstructors(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `instructor`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()


'''
    Course Queries
'''
def insertCourse(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `course`(`course_id`, `title`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showCourses(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `course`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()


'''
    Lesson Queries
'''
def insertLesson(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `lesson`(`lesson_id`, `title`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showLessons(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `lesson`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()

'''
    Contains Queries
'''
def insertContain(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `contains`(`course_id`, `lesson_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showContains(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `contains`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()


'''
    Learns Queries
'''
def insertLearn(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `learns`(`student_id`, `course_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showLearns(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `learns`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()


'''
    Teachs Queries
'''
def insertTeach(items,oneOrMany,cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    sql = "INSERT INTO `teaches`(`instructor_id`, `course_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    #connectDB.commit()
    #cursorDB.close()
    #connectDB.close()

def showTeachs(cursorDB):
    #connectDB = Connect()
    #cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `teaches`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    #cursorDB.close()
    #connectDB.close()

def insertQueries(instructorNum,studentNum,courseNum):
    connectDB = Connect()
    cursorDB = connectDB.cursor()
    '''
        fill the course,lesson,contain tables
    '''
    for courseID in range(1,courseNum+1):
        title,lessonTitles,lessonIDs = course(courseID)
        lessons = []
        contains = []
        for i in range(0,len(lessonTitles)):
            lessons.append((lessonIDs[i],lessonTitles[i]))
            contains.append((courseID,lessonIDs[i]))
        insertCourse((courseID,title),0,cursorDB)
        insertLesson(lessons,1,cursorDB)
        insertContain(contains,1,cursorDB)
    
    '''
        fill the student,learn table
    '''
    for studID in range(1,studentNum+1):
        fname,lname,year = student()
        insertStudent((studID,fname,lname,year),0,cursorDB)
        learn = []
        coursesRange = studentCourse()
        for courseID in coursesRange:
            learn.append((studID,courseID,cursorDB))
        insertLearn(learn,1,cursorDB)

    '''
        fill the instructor,teach table
    '''
    for instructorID in range(1,instructorNum+1):
        fname,lname,degree = instructor()
        insertInstructor((instructorID,fname,lname,degree),0,cursorDB)
        teach = []
        coursesRange = instructorCourse()
        for courseID in coursesRange:
            teach.append((instructorID,courseID))
        insertTeach(teach,1,cursorDB)
    
    connectDB.commit()
    cursorDB.close()
    connectDB.close()


insertQueries(10,50,40)