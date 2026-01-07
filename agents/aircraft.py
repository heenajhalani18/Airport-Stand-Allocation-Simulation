from mesa import Agent

class AircraftAgent(Agent):
    def __init__(self, unique_id, model, arrival_time, departure_time):
        super().__init__(model)   # model is now VALID

        self.unique_id = unique_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time

        self.state = "scheduled"
        self.assigned_stand_type = None

    def arrive(self):
        self.state = "arrived"

    def park(self, stand_type):
        self.assigned_stand_type = stand_type
        self.state = "parked"

    def depart(self):
        self.state = "departed"
