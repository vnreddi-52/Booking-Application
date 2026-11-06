import re
from datetime import date, datetime

phone_no_pattern = r"^[6-9]\d{9}$"
email_pattern = r"^[a-zA-Z0-9]+@gmail\.com$"
guest_pattern = r"^[1-9]$"

def validate_guest_input():
    phone_no = input("Enter phone number: ")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    no_of_guests = input("Enter no of guests: ")
    check_in = input("Enter check_in date: ")
    check_out = input("Enter check_out date: ")

    return phone_no, name, email, no_of_guests, check_in, check_out

def get_room_type(msg):
    while True:
        type = input(msg).strip()

        if type.lower() in ("standard", "deluxe", "suite"):
            return type.capitalize()

        print("Invalid Room type")
        
def get_date(msg):
    while True:
        try:
            i_date = input(msg)

            parsed_date = datetime.strptime(i_date, "%d-%m-%Y")
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date entered")
            