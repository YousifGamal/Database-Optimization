from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
import random


dbUrl = "mongodb://localhost:27017"


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(dbUrl)


def createUserObj(items, oneOrMany=0):
    if oneOrMany == 0:
        object = {
            "id": items[0],
            "fname": items[1],
            "lastname": items[2],
            "type": items[3],
            "degree": items[4],
            "year": items[5],
            "courses": items[6]}

        return object
    else:
        objArr = []
        for item in items:
            object = {
                "id": item[0],
                "fname": item[1],
                "lastname": item[2],
                "type": item[3],   # 0 for student and 1 for instructor
                "degree": item[4],
                "year": item[5],
                "courses": item[6]}
            objArr.append(object)
        return objArr


def insertUser(items, oneOrMany=0):

    connection = Connect.get_connection()

    db = connection.projectDB_10k

    obj = createUserObj(items, oneOrMany)

    if oneOrMany == 0:
        db.users.insert_one(obj)
    else:
        db.users.insert_many(obj)


def showUsers():
    connection = Connect.get_connection()

    db = connection.projectDB_10k
    cursor = db.users.find({})
    for x in cursor:
        pprint(x)


def createCourserObj(items, oneOrMany=0):
    if oneOrMany == 0:
        object = {
            "id": items[0],
            "title": items[1],
            "lessons": items[2]}

        return object
    else:
        objArr = []
        for item in items:
            object = {
                "id": item[0],
                "title": item[1],
                "lessons": item[2]}
            objArr.append(object)
        return objArr


def insertCourse(items, oneOrMany=0):

    connection = Connect.get_connection()

    db = connection.projectDB_10k

    obj = createCourserObj(items, oneOrMany)

    if oneOrMany == 0:
        db.courses.insert_one(obj)
    else:
        db.courses.insert_many(obj)


def showCourses():
    connection = Connect.get_connection()

    db = connection.projectDB_10k
    cursor = db.courses.find({})
    for x in cursor:
        print(x)

# 1 - test to insert one item at users collections


#user_item = [random.randint(1, 100), "khaled", "Galal",
#             random.randint(0, 1), "Degree" + str(random.randint(1, 5)), "2020", [{"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}]]
#insertUser(user_item, 0)
#showUsers()

# 2 -  test to insert more than one item at users collections

# user_items = [[random.randint(1, 100), "khaled", "Galal",
#                random.randint(0, 1), "Degree" + str(random.randint(1, 5)), "2020", [{"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}]], [random.randint(1, 100), "khaled", "Galal",
#                                                                                                                                                                                            random.randint(0, 1), "Degree" + str(random.randint(1, 5)), "2020", [{"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}, {"courseId": random.randint(1, 5)}]]]
# insertUser(user_items, 1)
# showUsers()

# 3 -test to insert one item at courses collections

# course_item = [random.randint(1, 100), "title" +
#                str(random.randint(1, 5)), [{"id": random.randint(1, 5), "title": "title" +
#                                             str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                          str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                                                       str(random.randint(1, 5))}]]
# insertCourse(course_item, 0)
# showCourses()


# 4 - test to insert more than one item at courses collections

# course_items = [[random.randint(1, 100), "title" +
#                  str(random.randint(1, 5)), [{"id": random.randint(1, 5), "title": "title" +
#                                               str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                            str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                                                         str(random.randint(1, 5))}]], [random.randint(1, 100), "title" +
#                                                                                                                                        str(random.randint(1, 5)), [{"id": random.randint(1, 5), "title": "title" +
#                                                                                                                                                                     str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                                                                                                                                                  str(random.randint(1, 5))}, {"id": random.randint(1, 5), "title": "title" +
#                                                                                                                                                                                                                               str(random.randint(1, 5))}]]]
# insertCourse(course_items, 1)
# showCourses()
