class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor
        
    
elevator = Elevator(1)
print(elevator.make)
print(elevator.floor)