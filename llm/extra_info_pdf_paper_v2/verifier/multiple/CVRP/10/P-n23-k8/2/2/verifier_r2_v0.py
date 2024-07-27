import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the demand at each city
demands = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 
    14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

# Define robot tours and their reported costs
robot_tours = {
    0: ([0, 2, 0], 42.05),
    1: ([0, 4, 0], 44.05),
    2: ([0, 3, 18, 19, 0], 92.62),
    3: ([0, 9, 17, 13, 0], 85.54),
    4: ([0, 5, 14, 22, 0], 67.94),
    5: ([0, 10, 11, 12, 15, 0], 91.60),
    6: ([0, 1, 8, 0], 67.22),
    7: ([0, 6, 16, 0], 28.44),
    8: ([0, 7, 20, 21, 0], 47.08),
}

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify solution
def verify_solution():
    total_cost_verified = 0
    delivered_demands = {city: 0 for city in cities}

    # Verify each robot's tour
    for robot, (tour, reported_cost) in robot_tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour must start and end at the depot.")
            return "FAIL"
        
        # Total demand and calculate the actual cost
        tour_demand = 0
        actual_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            actual_cost += calculate_distance(city_from, city_to)
            if i > 0:  # Skip depot for demand tallying
                tour_demand += demands[city_to]

        if round(actual_cost, 2) != reported_cost:
            print(f"FAIL: Reported cost and calculated cost do not match for robot {robot}: {reported_cost} vs {round(actual_cost, 2)}")
            return "FAIL"
        
        if tour_demand > 40:
            print(f"FAIL: Capacity exceeded for robot {robot}.")
            return "FAIL"

        # Sum demands
        for city in tour[1:-1]:  # Exclude the depot
            delivered_demands[city] += demands[city]

    # Check if all demands are met exactly
    if any(demand != delivered_demands[city] for city, demand in demands.items() if city != 0):  # Exclude depot from demand check
        print("FAIL: Not all demands are fully met.")
        return "FAIL"

    return "CORRECT"

# Check and output the result of the verification
verification_result = verify_solution()
print(verification_result)