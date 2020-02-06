import pprint
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')

db = client['CS4DS']
students = db.students

y = True
while y == True:  # Menu
    menu = int(input("What would you like? \n\
    1. Insert \n\
    2. Delete \n\
    3. Update \n\
    4. View All Students \n\
    0. To Exit \n"))

    if menu == 1:  # Inset
        print("Please enter Student Info:")
        name = str(input("Name: "))
        degree = str(input("Degree: "))
        age = str(input("Age: "))
        sem = str(input("Semester: "))
        s_id = str(input("id: "))
        student = {
            'id': s_id,
            'name': name,
            'degree': degree,
            'age': age,
            'semester': sem
        }
        result = students.insert_one(student)
        if result.acknowledged:
            print("Student Added: " + str(result.inserted_id))

    elif menu == 2:  # Delete
        s_id = input(
            "Please enter the student's ID to whome you want to delete: ")
        students.delete_one({
            'id': s_id
        })
        print("Student against " + s_id + " is deleted.")
    elif menu == 3:  # Update
        s_id = input(
            "Please enter the student's ID to whome you want to update: ")
        print("Please enter Student Info:")
        name = str(input("Name: "))
        degree = str(input("Degree: "))
        age = str(input("Age: "))
        sem = str(input("Semester: "))

        result = students.update({
            'id': s_id
        },
            {
                '$set': {
                    'name': name,
                    'degree': degree,
                    'age': age,
                    'semester': sem
                }
        }, multi=False)
    elif menu == 4:  # View All
        print("Here is a list of all students")
        listOfStudents = students.find()
        for x in listOfStudents:
            pprint.pprint(x)
    elif menu == 0:  # Exit
        exit()
    else:
        pprint.pprint("Invalid option ")
        y = False
