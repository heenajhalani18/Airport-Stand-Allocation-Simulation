# Airport Stand Allocation Simulation

## Overview

This project implements a simplified airport operations simulation focused on aircraft stand allocation over a fixed operational window. Aircraft arrive and depart over time and must be assigned to available stands during their ground time.

Two types of stands are modeled:

- **PLB (Passenger Loading Bridge) stands** – limited and preferred
- **Remote stands** – unlimited fallback

The simulation runs over a 6-hour window using discrete time steps and produces structured outputs that support post-simulation analytics on resource utilization and operational load.

## What Was Built

- An **agent-based simulation** using Mesa, where each aircraft is modeled as an agent
- A centralized **AirportModel** that controls time progression, stand allocation, and resource release
- Event and state logging to support analytics
- Post-simulation analytics to evaluate resource efficiency and congestion

The design prioritizes clarity, determinism, and explainability over real-world operational complexity.

## High-Level Working of the Simulation

1. Time advances in discrete steps (each step represents 5 minutes).
2. At each step:
   - Aircraft scheduled for arrival enter the system.
   - Newly arrived aircraft are assigned a stand:
     - PLB is assigned if available.
     - Otherwise, a Remote stand is assigned.
   - Aircraft occupy their assigned stand until their departure time.
   - On departure, PLB stands are released back to the pool.
3. The model logs:
   - Aircraft lifecycle events (arrival, assignment, departure)
   - System-level state at each time step (active aircraft count, PLB occupancy)

After the simulation completes, analytics are computed from the logged data.

## How to Run

### Requirements

- Python 3.8+
- Mesa

Install Mesa:

```bash
pip install mesa

```
### Run Command

The project is structured as a Python package and should be run from the parent directory:

python3 -m airport_simulation.main

## Inputs

Aircraft input data is provided via a CSV file:
-data/input_aircraft.csv

### Expected Columns

-aircraft_id – Unique aircraft identifier
-arrival_time – Arrival time (simulation step)
-departure_time – Departure time (simulation step)

Time values are represented using discrete simulation steps.

## Outputs

During execution, the simulation collects structured in-memory logs, including:
-Aircraft lifecycle events (arrival, stand assignment, departure)
-System state at each time step:

1. Number of active aircraft
2. Number of PLB stands occupied

After the simulation finishes, summary analytics are computed and displayed.

## Metrics Calculated

1. **PLB Utilization Rate**
   Measures how efficiently the limited PLB stands are used across the simulation window.

2. **Aircraft Assigned to PLB (%)**
   Indicates quality of service by showing how many aircraft received preferred stands.

3. **Peak Concurrent Aircraft**
   Represents the maximum number of aircraft on the ground at any point, highlighting congestion periods.

The logged data supports extending analytics with additional metrics if required.

## Assumptions and Trade-offs

1. PLB stands are the only constrained resource; remote stands are assumed to be unlimited.

2. Stand allocation follows a simple deterministic rule (PLB preferred).

3. Aircraft behavior is modeled using a minimal lifecycle abstraction.

4. Real-world airport rules, constraints, and optimizations are intentionally not modeled.

These choices were made to keep the simulation easy to understand, explain, and extend.
