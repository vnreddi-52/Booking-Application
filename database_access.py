# Queries for Room
create_query_room = """CREATE TABLE IF NOT EXISTS ROOM(
                room_no INT PRIMARY KEY,
                room_type TEXT NOT NULL CHECK(room_type in ('Standard','Deluxe','Suite')),
                floor INT NOT NULL CHECK(floor BETWEEN 1 AND 3),
                is_available BOOL NOT NULL CHECK(is_available in ('True','False'))
                )
                """

select_query_room = """SELECT * FROM ROOM"""

insert_query_room = """INSERT OR IGNORE INTO ROOM VALUES (?,?,?,?)"""

# def initialise_databases():
#     curr.execute(insert_query_room)
