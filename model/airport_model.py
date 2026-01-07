from mesa import Model
from airport_simulation.agents.stand import Stand

class AirportModel(Model):

    def __init__(self, aircraft_agents, num_plb_stands, max_steps):
        super().__init__()   # ✅ THIS IS THE FIX

        self.current_step = 0
        self.max_steps = max_steps

        self.all_aircraft = aircraft_agents
        self.active_aircraft = []

        self.plb_stands = [Stand(f"PLB_{i}") for i in range(num_plb_stands)]

        self.event_log = []
        self.time_state_log = []

    # ---- Helper: find free PLB stand ----
    def get_free_plb_stand(self):
        for stand in self.plb_stands:
            if not stand.is_occupied:
                return stand
        return None

    # ---- Core simulation step ----
    def step(self):
        self.current_step += 1

        # 1. Handle arrivals
        for aircraft in self.all_aircraft:
            if aircraft.arrival_time == self.current_step:
                aircraft.arrive()
                self.active_aircraft.append(aircraft)
                self.event_log.append({
                    "time": self.current_step,
                    "aircraft_id": aircraft.unique_id,
                    "event": "arrival"
                })

        # 2. Assign stands
        for aircraft in self.active_aircraft:
            if aircraft.state == "arrived":
                free_stand = self.get_free_plb_stand()
                if free_stand:
                    free_stand.occupy(aircraft.unique_id)
                    aircraft.park("PLB")
                else:
                    aircraft.park("Remote")

                self.event_log.append({
                    "time": self.current_step,
                    "aircraft_id": aircraft.unique_id,
                    "event": "assigned",
                    "stand_type": aircraft.assigned_stand_type
                })

        # 3. Handle departures
        for aircraft in list(self.active_aircraft):
            if aircraft.departure_time == self.current_step:
                if aircraft.assigned_stand_type == "PLB":
                    for stand in self.plb_stands:
                        if stand.aircraft_id == aircraft.unique_id:
                            stand.release()

                aircraft.depart()
                self.active_aircraft.remove(aircraft)

                self.event_log.append({
                    "time": self.current_step,
                    "aircraft_id": aircraft.unique_id,
                    "event": "departure"
                })

        # 4. Log system state
        self.time_state_log.append({
            "time": self.current_step,
            "active_aircraft": len(self.active_aircraft),
            "plb_occupied": sum(1 for s in self.plb_stands if s.is_occupied)
        })
