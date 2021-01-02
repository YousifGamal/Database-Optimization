from connect import Connect


'''
    Students Queries
'''
def insertStudent(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `student`(`student_id`, `first_name`, `last_name`, `year`) VALUES (%s,%s,%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showStudents():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `student`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()

'''
    Instructor Queries
'''
def insertInstructor(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `instructor`(`instructor_id`, `first_name`, `last_name`, `degree`) VALUES (%s,%s,%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showInstructors():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `instructor`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()


'''
    Course Queries
'''
def insertCourse(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `course`(`course_id`, `title`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showCourses():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `course`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()


'''
    Lesson Queries
'''
def insertLesson(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `lesson`(`lesson_id`, `title`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showLessons():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `lesson`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()

'''
    Contains Queries
'''
def insertContain(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `contains`(`course_id`, `lesson_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showContains():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `contains`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()


'''
    Learns Queries
'''
def insertLearn(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `learns`(`student_id`, `course_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showLearns():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `learns`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()


'''
    Teachs Queries
'''
def insertTeach(items,oneOrMany):
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    sql = "INSERT INTO `teaches`(`instructor_id`, `course_id`) VALUES (%s,%s)"
    
    values = items
    if oneOrMany == 0:
        cursorDB.execute(sql,values)
    else:
        cursorDB.executemany(sql, values)

    connectDB.commit()
    cursorDB.close()
    connectDB.close()

def showTeachs():
    connectDB = Connect()
    cursorDB = connectDB.cursor()

    cursorDB.execute("SELECT * FROM `teaches`")
    results = cursorDB.fetchall()

    for row in results:
        print(row)
    
    cursorDB.close()
    connectDB.close()