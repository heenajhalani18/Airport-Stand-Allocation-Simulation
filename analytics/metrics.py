def compute_metrics(model):
    total_steps = len(model.time_state_log)
    total_plb_capacity = total_steps * len(model.plb_stands)

    plb_occupied_time = sum(
        entry["plb_occupied"] for entry in model.time_state_log
    )

    plb_utilization = plb_occupied_time / total_plb_capacity if total_plb_capacity else 0

    total_aircraft = len(model.all_aircraft)
    plb_aircraft = sum(
        1 for a in model.all_aircraft if a.assigned_stand_type == "PLB"
    )

    peak_concurrency = max(
        entry["active_aircraft"] for entry in model.time_state_log
    )

    return {
        "PLB Utilization Rate": round(plb_utilization, 2),
        "Aircraft Assigned to PLB (%)": round((plb_aircraft / total_aircraft) * 100, 2),
        "Peak Concurrent Aircraft": peak_concurrency
    }
