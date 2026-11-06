
class Queries:
    # Queries for Room
    create_query_room = """CREATE TABLE IF NOT EXISTS ROOM(
                        room_no INT PRIMARY KEY,
                        room_type TEXT NOT NULL CHECK(room_type in ('Standard','Deluxe','Suite')),
                        floor INT NOT NULL CHECK(floor BETWEEN 1 AND 3),
                        is_available BOOL NOT NULL CHECK(is_available in ('True','False'))
                        )
                        """
    insert_query_room = """INSERT OR IGNORE INTO ROOM VALUES (?,?,?,?)"""
    select_query_room = """SELECT * FROM ROOM"""

    # Quesries for Guests 
    create_query_guest = """CREATE TABLE IF NOT EXISTS GUEST (
                        phone_no TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL
                        )"""

    insert_query_guest = """INSERT OR IGNORE INTO Guest VALUES
                        ('9876543210', 'Rahul Sharma', 'rahul@gmail.com'),
                        ('8765432109', 'Priya Reddy', 'priya@gmail.com'),
                        ('7654321098', 'Arjun Kumar', 'arjun@gmail.com'),
                        ('9123456780', 'Sneha Rao', 'sneha@gmail.com'),
                        ('9988776655', 'Karthik Nair', 'karthik@gmail.com'),
                        ('8877665544', 'Ananya Das', 'ananya@gmail.com'),
                        ('7788990011', 'Vikram Singh', 'vikram@gmail.com'),
                        ('6677889900', 'Meera Joshi', 'meera@gmail.com'),
                        ('9090909090', 'Aditya Verma', 'aditya@gmail.com'),
                        ('7894561230', 'Divya Menon', 'divya@gmail.com');"""


    select_query_guest = """SELECT * FROM GUEST"""

    # QUeries for Booking
    create_query_booking = """ CREATE TABLE IF NOT EXISTS Booking (
                            bid INTEGER PRIMARY KEY AUTOINCREMENT,
                            guest INT NOT NULL REFERENCES GUEST(phone_no),
                            room INT NOT NULL REFERENCES ROOM(room_no),
                            booking_date DATE NOT NULL,
                            check_in DATE NOT NULL ,
                            check_out DATE NOT NULL ,
                            no_of_guests INT NOT NULL,
                            status TEXT NOT NULL,
                            price REAL NOT NULL,
                            cancelled_date DATE
                            )"""
    insert_query_booking= """INSERT OR IGNORE INTO Booking
                            (bid, guest, room, booking_date, check_in, check_out,
                            no_of_guests, status, price, cancelled_date)
                            VALUES

                            (1, 9876543210, 101, '2026-11-06', '2026-11-10', '2026-11-13', 2, 'CONFIRMED', 8400.0, NULL),
                            (2, 8765432109, 201, '2026-11-06', '2026-11-12', '2026-11-16', 3, 'CONFIRMED', 23296.0, NULL),
                            (3, 7654321098, 101, '2026-11-06', '2026-11-13', '2026-11-15', 2, 'CONFIRMED', 5000.0, NULL),
                            (4, 9123456780, 102, '2026-11-06', '2026-11-10', '2026-11-18', 2, 'CONFIRMED', 18000.0, NULL),
                            (6, 8877665544, 202, '2026-11-06', '2026-11-20', '2026-11-22', 1, 'CONFIRMED', 8000.0, NULL),
                            (7, 7788990011, 103, '2026-11-03', '2026-11-06', '2026-11-09', 2, 'CHECKED_IN', 8400.0, NULL),
                            (8, 6677889900, 302, '2026-11-03', '2026-11-06', '2026-11-12', 3, 'CHECKED_IN', 52000.0, NULL),
                            (9, 9090909090, 203, '2026-10-15', '2026-10-20', '2026-10-23', 3, 'CHECKED_OUT', 15000.0, NULL),
                            (10, 7894561230, 303, '2026-10-20', '2026-10-25', '2026-10-30', 4, 'CHECKED_OUT', 45000.0, NULL),
                            (11, 9876543210, 102, '2026-11-01', '2026-12-20', '2026-12-23', 2, 'CANCELLED', 8400.0, '2026-11-06'),
                            (12, 8765432109, 202, '2026-11-05', '2026-11-12', '2026-11-15', 2, 'CANCELLED', 12000.0, '2026-11-08'),
                            (13, 7654321098, 203, '2026-11-06', '2026-11-08', '2026-11-10', 2, 'CANCELLED', 8000.0, '2026-11-07'),
                            (14, 9876543210, 201, '2026-09-05', '2026-09-10', '2026-09-13', 2, 'CHECKED_OUT', 12000.0, NULL),
                            (15, 9876543210, 202, '2026-09-15', '2026-09-20', '2026-09-23', 2, 'CHECKED_OUT', 12000.0, NULL),
                            (16, 9876543210, 203, '2026-09-25', '2026-10-01', '2026-10-04', 2, 'CHECKED_OUT', 12000.0, NULL),
                            (17, 9123456780, 301, '2026-11-06', '2026-12-01', '2026-12-09', 2, 'CONFIRMED', 60000.0, NULL),
                            (18, 9988776655, 103, '2026-11-06', '2026-12-10', '2026-12-12', 2, 'CONFIRMED', 5000.0, NULL),
                            (19, 8877665544, 201, '2026-11-06', '2026-12-15', '2026-12-18', 3, 'CONFIRMED', 18000.0, NULL),
                            (20, 7788990011, 302, '2026-11-06', '2026-12-20', '2026-12-24', 4, 'CONFIRMED', 36000.0, NULL)
                            """
    
    select_query_booking = """SELECT * FROM BOOKING"""

    room_availability_query = """
                SELECT r.room_no
                from Room r
                where r.room_type = ?
                AND r.room_no NOT IN (
                SELECT b.room 
                from booking b
                where b.status in ('CONFIRMED', 'CHECKED_IN') AND
                 ? < b.check_out AND
                ? > b.check_in
                )
                ORDER BY r.room_no ASC
                """


