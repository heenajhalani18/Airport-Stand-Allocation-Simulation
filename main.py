from airport_simulation.data.data_loader import load_aircraft_data
from airport_simulation.model.airport_model import AirportModel
from airport_simulation.agents.aircraft import AircraftAgent
from airport_simulation.analytics.metrics import compute_metrics
import os

# --------------------
# Configuration
# --------------------
MAX_STEPS = 72
NUM_PLB_STANDS = 3

# --------------------
# Load input data
# --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "input_aircraft.csv")

aircraft_data = load_aircraft_data(csv_path)

# --------------------
# Initialize model
# --------------------
model = AirportModel(
    aircraft_agents=[],   # will add agents after creation
    num_plb_stands=NUM_PLB_STANDS,
    max_steps=MAX_STEPS
)

# --------------------
# Create agents (NOW model exists)
# --------------------
aircraft_agents = []
for row in aircraft_data:
    agent = AircraftAgent(
        unique_id=row["aircraft_id"],
        model=model,
        arrival_time=row["arrival_time"],
        departure_time=row["departure_time"]
    )
    aircraft_agents.append(agent)

# Attach agents to model
model.all_aircraft = aircraft_agents

# --------------------
# Run simulation
# --------------------
for _ in range(MAX_STEPS):
    model.step()

# --------------------
# Compute metrics
# --------------------
metrics = compute_metrics(model)

print("\n--- Simulation Metrics ---")
for k, v in metrics.items():
    print(f"{k}: {v}")
