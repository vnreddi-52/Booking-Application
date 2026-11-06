import csv 
import sqlite3 as sq
from models import StandardRoom, DeluxeRoom, SuiteRoom
from database_access import Queries
from validations import get_date, validate_guest_input, get_room_type
import math 

ROOM_CAPACITY = {
    "Standard": 2,
    "Deluxe": 3,
    "Suite": 5
}

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

        curr.execute(Queries.insert_query_room, (room_no, room_type, floor, 'True'))
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

def initialise_databases():
    curr.execute("PRAGMA foreign_keys = OFF")
    curr.execute("DROP TABLE IF EXISTS Booking")
    curr.execute("DROP TABLE IF EXISTS Guest")
    curr.execute("DROP TABLE IF EXISTS Room")
    print("Dropped succesfully")

    curr.execute(Queries.create_query_room)
    rooms_data = list(load_rooms_csv())
    validate_data(rooms_data)

    curr.execute(Queries.create_query_guest)
    curr.execute(Queries.insert_query_guest)

    curr.execute(Queries.create_query_booking)
    curr.execute(Queries.insert_query_booking)

    conn.commit()
    
    curr.execute("PRAGMA foreign_keys = ON")

def display_tables():
    curr.execute(Queries.select_query_room)
    for i in curr.fetchall():
        print(i)

    curr.execute(Queries.select_query_guest)
    for i in curr.fetchall():
        print(i)

    curr.execute(Queries.select_query_booking)
    for i in curr.fetchall():
        print(i) 

def display(obj):
    for i in obj:
        print(i)

rooms_data = list(load_rooms_csv())
validate_data(rooms_data)

def get_input_case1():
    room_type = get_room_type("Enter the type of room needed: ").strip().capitalize()
    check_in = get_date("Enter check_in date: ")
    check_out = get_date("Enter check_out date: ")
    while True:
        try:
            no_of_guests = int(input("Enter no of guests: "))
            if no_of_guests>0:
                break
            print("NUmber of guests must be greater than 0")
        except ValueError:
            print("Enter a valid number")
    return room_type, check_in, check_out, no_of_guests

def check_availability(room_type, check_in, check_out, no_of_guests):
    capacity = ROOM_CAPACITY[room_type]
    required_rooms = math.ceil(no_of_guests/capacity)
    curr.execute(Queries.room_availability_query, (room_type, check_in, check_out))

    
    # print("inpuuf:", room_type, check_in, check_out)
    # print("sql eresulgt:", curr.fetchall())
    available_rooms = [row[0] for row in curr.fetchall()] 
    if len(available_rooms)>=required_rooms:
        return available_rooms[:required_rooms]
    return []

def alternative_rooms(room_type, check_in, check_out, no_of_guests):
    alternatives = {}

    for r_type, r_capacity in ROOM_CAPACITY.items():
        if r_type == room_type:
            continue
        required_rooms = required_rooms = math.ceil(no_of_guests/r_capacity)
        curr.execute(Queries.room_availability_query, (r_type, check_in, check_out))
        available_rooms = [row[0] for row in curr.fetchall()]
        if len(available_rooms)>=required_rooms:
            alternatives[r_type] = available_rooms[:required_rooms]
    return alternatives
    
def create_booking():
    # guest details
    phone_no, name, email, no_of_guests, check_in, check_out = validate_guest_input()
    
    # create booking details
    pass
    

