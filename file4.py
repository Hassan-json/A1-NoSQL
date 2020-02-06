import redis
import pprint


client = redis.Redis(host='localhost', port=6379, db=0)
client.set('foo', 'bar')
print(client.get('foo'))

y = True
while y == True:  # Menu
    menu = int(input("Connected with Redis Server: What would you like? \n\
    1. Insert \n\
    2. Delete \n\
    3. Update \n\
    4. View Student\n\
    5. View All Students\n\
    0. To Exit \n"))

    if menu == 1:  # Insert
        print("Please enter Student Info:")
        name = str(input("Name:"))
        s_id = str(input("id:"))
        client.hset("Students", s_id, name)
        print("Student Added")

    elif menu == 2:  # Delete
        s_id = input("Please enter the student's ID to whome you want to delete: ")
        client.hdel("Students", s_id)
        print("Student against " + s_id + " is deleted.")
    elif menu == 3:  # Update
        s_id = input(
            "Please enter the student's ID to whome you want to update: ")
        name = str(input("Name: "))
        result = client.hset("Students", s_id, name)
    elif menu == 4:  # View Against Key
        print("Here is your required student")
        s_id = str(input("id:"))
        print(client.hget("Students", s_id))

    elif menu == 5:  # View All
        print(client.hgetall("Students"))

    elif menu == 0:  # Exit
        exit()
    else:
        pprint.pprint("Invalid option ")
        y = False
