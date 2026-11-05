from abc import ABC, abstractmethod

DAYS = ["Friday", "Saturday"]

class Room(ABC):
    def __init__(self, room_no, room_type, floor):
        self.room_no = room_no
        self.room_type = room_type
        self.floor = floor

    @abstractmethod
    def tariff(self, check_in, check_out):
        pass
    @abstractmethod
    def extra_guest(self):
        pass
    @abstractmethod
    def breakfast(self):
        pass

class StandardRoom(Room):
    def __init__(self, room_no, room_type, floor):
        super().__init__(room_no, room_type, floor)
        self.base_rate = 2500
        self.max_guests=2
        
    def tariff(self, day):
        if not day.capitalize() in DAYS:
            pass
        else:
            pass
   
    def extra_guest(self, ):
        pass

    def breakfast(self):
        pass

    def __str__(self):
        return f"{self.room_no} {self.room_type} {self.floor}"

class DeluxeRoom(Room):
    def __init__(self, room_no, room_type, floor):
        super().__init__(room_no, room_type, floor)
        self.base_rate = 4000
        self.max_guests=3

    def tariff(self):
        pass
    
    def extra_guest(self):
        pass

    def breakfast(self):
        pass

    def __str__(self):
        return f"{self.room_no} {self.room_type} {self.floor}"
    
class SuiteRoom(Room):
    def __init__(self, room_no, room_type, floor):
        super().__init__(room_no, room_type, floor)
        self.base_rate = 7500
        self.max_guests=4

    def tariff(self):
        pass
    
    def extra_guest(self):
        pass

    def breakfast(self):
        pass

    def __str__(self):
        return f"{self.room_no} {self.room_type} {self.floor}"

class Booking:
    def __init__(self,):
        pass