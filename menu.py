from main import conn, curr, check_availability, validate_data, load_rooms_csv

def create_booking():
    pass

def check_in():
    pass

def check_out():
    pass

def cancel_booking():
    pass

def view_booking_details():
    pass

def guest_stay_history():
    pass

def occupancy_report():
    pass

def revenue_report():
    pass

def export_bookings():
    pass

def menu():
    rooms_data = list(load_rooms_csv())
    validate_data(rooms_data)
    # for i in rooms_data:
    #     print(i)
    while True:
        print("""
              1. Search room availability
              2. Create Booking
              3. Check in
              4. CHeck out
              5. Cancel Booking
              6. View booking details
              7. Guest stay history 
              8. Occupancy report
              9. Revenue report
              10. Export all bookings to CSV
              11. Exit 
            """)

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                check_availability()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                print("Exiting")
                return

menu()