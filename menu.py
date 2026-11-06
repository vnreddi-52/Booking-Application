from main import conn, curr, check_availability, initialise_databases, display_tables, alternative_rooms, get_input_case1

def display_list(list_type):
    if not list_type:
        print("No values to return")
        return []
    else:
        for i in list_type:
            print(i)

def menu():
    initialise_databases()
    # display_tables()

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
                room_type, check_in, check_out, no_of_guests = get_input_case1()
                # curr.execute("SELECT * FROM ROOM WHERE room_type = 'Standard'")
                data = check_availability(room_type, check_in, check_out, no_of_guests)
                if data:
                    print(f"Available {room_type} Rooms are:")
                    display_list(data)
                else:
                    print("No rooms avaliable of your type")
                    data2 = alternative_rooms(room_type, check_in, check_out, no_of_guests)
                    if data2:
                        print("Other room types are")

                        for r_type, rooms in data2.items():
                            print(f"{r_type}: {rooms}")
                    else:
                        print("Sorru bro no rooms available at all")
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