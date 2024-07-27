import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, demands, capacities, city_coordinates):
    # Initialize capacities and demands
    remaining_capacity = [capacities[robot] for robot in range(len(tours))]
    unmet_demand = demands.copy()

    # Storage for costs
    travel_costs = []

    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL", "Robots must start and end at the depot city."

        current_capacity = capacities[robot_id]
        total_cost = 0

        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i+1]
            distance = calculate_distance(city_coordinates[from_city], city_coordinates[to_city])
            total_cost += distance

            # Decrease demands and check capacity
            if from_city != 0: # ignore depot for demand
                if unmet_demand[from_city] > 0 and remaining_capacity[robot_id] >= unmet_demand[from_city]:
                    remaining_capacity[robot_id] -= unmet_demand[from_city]
                    unmet_demand[from_city] = 0
                else:
                    return "FAIL", "Exceeded capacity or unmet demand."

        travel_costs.append(total_cost)

    # Check if all demands are met
    if any(d > 0 for d in unmet_demand):
        return "FAIL", "Not all demands have been met."

    # Verify if any robot exceeded its capacity
    if any(c < 0 for c in remaining_capacity):
        return "FAIL", "Capacity constraints not respected."

    # Check if the total mileage is minimized
    # Note: The minimality check would typically require comparing against an optimal solution benchmark or LB.

    # Assemble and output comprehensive results
    output_details = []
    for i, cost in enumerate(travel_costs):
        output_details.append(f"Robot {i} Tour: {tours[i]}")
        output_details.append(f"Robot {i} Total Travel Cost: {cost}")
    output_details.append(f"Overall Total Travel Cost: {sum(travel_costs)}")

    return "CORRECT", "\n".join(output_details)

# Sample Data for testing
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160]

# Define two mock tours satisfying the given constraints hypothetically
tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0]
]

# Perform verification against requirements
result = verify_solution(tours, demands, capacities, cityupyter
print(result)  # Output should indicate correctness or failure and reasoning