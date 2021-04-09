
def addStudent(*args):
    Students = dict(args[4])
    GradeList = list(args[5])

    #Create new grade information
    newStudent = {
        "Midterm" : args[1],
        "Project" : args[2],
        "Final"   : args[3]
    }
    passingGrade = (args[1] * 0.3) + (args[2] * 0.3) + (args[3] * 0.4)
    newStudent["PassingGrade"] = passingGrade

    #Add new student to student dict. and arrange passing grade list
    Students[args[0]] = newStudent
    GradeList.insert(len(GradeList), passingGrade)
    GradeList = sorted(GradeList)
    GradeList = reversed(GradeList)

    returnList = list()
    returnList.append(Students)
    returnList.append(GradeList)
    return returnList
    

def printStudents(Students):
    print("ALL STUDENTS & INFORMATIONS")
    for name,grades in Students.items():
        print(name + ": ")
        for typeOfGrade, grade in grades.items():
            print("\t{0}: {1:.2f}".format(typeOfGrade, grade))
    print()

def printGradeList(GradeList):
    print("STUDENT GRADE LIST (Highest to Lowest)")
    for i in GradeList:
        print("{:.2f}".format(i))
    print()

def main(*args):
    Students = {}
    GradeList = []
    
    # Read students' information and add them to database
    for stu in range(args[0]):
        print("---- Student {} ----".format(stu + 1))
        name = input("Please enter the name: ")
        midterm = int(float(input("What is midterm grade?: ")))
        project = int(float(input("What is project grade?: ")))
        final   = int(float(input("What is final grade?: ")))

        result = addStudent(name, midterm, project, final, Students, GradeList)
        Students = result[0]
        GradeList = result[1]
        print()
    
    printStudents(Students)
    printGradeList(GradeList)

main(5)
