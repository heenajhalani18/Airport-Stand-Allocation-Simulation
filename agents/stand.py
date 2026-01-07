class Stand:
    def __init__(self, stand_id):
        self.stand_id = stand_id
        self.is_occupied = False
        self.aircraft_id = None

    def occupy(self, aircraft_id):
        self.is_occupied = True
        self.aircraft_id = aircraft_id

    def release(self):
        self.is_occupied = False
        self.aircraft_id = None
