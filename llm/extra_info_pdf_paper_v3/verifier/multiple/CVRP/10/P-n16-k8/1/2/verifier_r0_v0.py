import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_robot_tours(tours, demands, capacities, coordinates):
    total_demand_met = [0] * len(demands)
    robot_capacities_used = []
    overall_travel_cost = 0

    for tour in tours:
        current_capacity = 0
        travel_cost = 0
        previous_city = tour[0]

        for city in tour[1:]:
            travel_cost += calculate_euclidean_distance(coordinates[previous_city][0], coordinates[previous_city][1], coordinates[city][0], coordinates[city][1])
            previous_city = city
            if city != 0:  # do not count depot
                current_capacity += demands[city]
                total_demand_met[city] += demands[city]

        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tour must start and end at depot
        
        robot_capacities_used.append(current_capacity)
        overall_travel_cost += travel_cost

    if any(capacity > capacities[0] for capacity in robot_capacities_used):
        return "FAIL"  # Capacity constraint violated

    if any(demand_met != demands[i] for i, demand_met in enumerate(total_demand_met)):
        return "FAIL"  # Demand not fully met

    if not math.isclose(overall_travel_cost, 499.44, abs_tol=1e-2):
        return "FAIL"  # Total travel cost does not match the specified solution

    return "CORRECT"

# Data based on the solution and constraints
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]  # Including depot
capacities = [35]  # Assuming all robots have the same capacity
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Tours provided
tours = [
    [0, 6, 0],
    [0, 1, 10, 13, 0],
    [0, 2, 0],
    [0, 4, 11, 0],
    [0, 7, 5, 9, 0],
    [0, 15, 12, 0],
    [0, 14, 3, 0],
    [0, 8, 0]
]

# Call the verification function
result = verify_robot_tours(tours, demands, capacities, coordinates)
result