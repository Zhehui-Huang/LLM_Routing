import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, demands, capacities, city_coordinates):
    remaining_capacity = capacities[:]
    unmet_demand = demands[:]
    travel_costs = []

    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL", "Tours must start and end at the depot city."

        travel_cost = 0
        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            travel_cost += calculate_distance(city_coordinates[from_city], city_coordinates[to_city])
            
            if to_city != 0:  # Skip depot when checking for demands and capacities
                demand_to_meet = min(unmet_demand[to_city], remaining_capacity[robot_id])
                remaining_capacity[robot_id] -= demand_to_meet
                unmet_demand[to_city] -= demand_to_meet

        travel_costs.append(travel_cost)
        if remaining_capacity[robot_id] < 0:
            return "FAIL", "Capacity constraints violated."

    if any(demand > 0 for demand in unmet_demand[1:]):  # Skip depot
        return "FAIL", "Not all demands have been met."

    return "CORRECT", f"Total Travel Cost: {sum(trail_costs)}"

# The following is a mock input scenario:
city_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62)]
demands = [0, 19, 30, 16, 23]
capacities = [160, 160]

# Hypothetical tour paths for two robots:
tours = [
    [0, 1, 0],  # Shortened for example purposes
    [0, 2, 3, 0]
]

# Invoke the test
verification_result, message = verify_solution(tours, demands, capacities, city_coordinates)
print(verification_result)  # Expected: "CORRECT" or "FAIL"
print(message)  # Contains total travel cost or failure reason