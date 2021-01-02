import names
import random

years = ["Prep","First","Second","Junior","Senior"]

degrees = ["Teaching Assistant", "Professor","Assistant Professor",
            "Lecturer","Research Assistant","Postdoctoral","PhD Student"]


courses = ["Logic Design","Data Structures","Algorithms","Circuits I","Physics I",
        "Physics II","Mathematics I","Mathematics II","Civil Engineering","Presentation Skills",
        "Microprocessor","Computer Graphics","Intro DBMS","Project Management","Power Engineering",
        "Mathematics III","Software Engineering","Multimedia","Circuits II","Signals",
        "Economics","Computer Architecture","Operating Systems","Communications","Numerical Analysis",
        "Marketing","Advanced OS","Advanced Programming","Control Engineering","Advanced DBMS",
        "Computer Security","Consultation","Testing","Modeling","Pattern Recognition",
        "Web Development","Machine Learning","Image Processing","Compilers","OOP",
        ]
courseIDs = list(range(1,41))

def studentCourse(courseIDs):
    return random.sample(courseIDs,k=24)
    
def instructorCourse(courseIDs):
    return random.sample(courseIDs,k=5)

def student(years):
    lname = names.get_last_name()
    fname = names.get_first_name()
    year  = random.choice(years)
    return lname,fname,year



def instructor(degrees):
    lname = names.get_last_name()
    fname = names.get_first_name()
    degree = random.choice(degrees)
    return lname, fname, degree

#id 1-40
def course(courses,id):
    title = courses[id-1]
    lessonTitles = []
    lessonIDs = []
    for i in range(6):
        lTitle = title + ": part "+str(i+1)
        lessonTitles.append(lTitle)
        lessonIDs.append((id-1)*6+i+1)
    return title, lessonTitles, lessonIDs

