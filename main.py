import csv 
import sqlite3 as sq
from models import StandardRoom, DeluxeRoom, SuiteRoom
from database_access import create_query_room, insert_query_room, select_query_room

conn = sq.connect("stay_easy.db")
curr = conn.cursor()

StandardRoom_Obj=[]
DeluxeRoom_Obj=[]
SuiteRoom_Obj=[]
rooms_available =[]

# Loading CSV
def load_rooms_csv():
    try:
        file = open("rooms.csv", "r")
        return csv.reader(file)
    except Exception as e:
        print(e)

def log_errors(errors):
    with open("app.log", "w") as file:
        for i in errors:
            file.write(i)
            file.write("\n")
            
def validate_data(data):
    curr.execute(create_query_room)
    errors=[]
   
    for line, row in enumerate(data, start=1):
        if line==1:
            continue

        if len(row)!=3:
            errors.append("Missing fields")

        room_no, room_type, floor = row
        valid = True

        try:
            room_no = int(room_no)
        except ValueError:
            valid = False
            errors.append(f"Line {line} - Room no should be digit")
            continue

        if room_type.capitalize() not in ("Standard", "Deluxe", "Suite"):
            valid = False
            errors.append(f"Line {line} - Invalid Room Type")
            continue

        if floor not in ("1","2","3"):
            valid = False
            errors.append(f"Line {line} - Invalid Floor")
            continue

        curr.execute(insert_query_room, (room_no, room_type, floor, 'True'))
        if valid:
            type = room_type
            if room_type.capitalize() == "Standard":
                s1 = StandardRoom(room_no, room_type, floor)
                StandardRoom_Obj.append(s1)
            elif room_type.capitalize() == "Deluxe":
                d1 = DeluxeRoom(room_no, room_type, floor)
                DeluxeRoom_Obj.append(d1)
            elif room_type.capitalize() == "Suite":
                s = SuiteRoom(room_no, room_type, floor)
                SuiteRoom_Obj.append(s)
                
    conn.commit()
    log_errors(errors)

def display(obj):
    for i in obj:
        print(i)


rooms_data = list(load_rooms_csv())
validate_data(rooms_data)

# display(StandardRoom_Obj)
# display(DeluxeRoom_Obj)
# display(SuiteRoom_Obj)

# print("Executing")
# curr.execute(select_query_room)
# for i in curr.fetchall():
#     print(i)


# Functions 

def check_availability():
    type = input("Enter the type of room needed: ").strip().capitalize()
    curr.execute(select_query_room)
    for i in curr.fetchall():
        if i[1].capitalize()==type.capitalize() and i[3]=='True':
            rooms_available.append((i[0],i[1]))
            print(i[0],i[1])



