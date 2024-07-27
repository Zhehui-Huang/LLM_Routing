import numpy as np

# Coordinates of all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Robot tours (Index of depot is included in each list)
robot_tours = [
    [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], 
    [0, 18, 19, 3, 8, 14, 17, 9, 13, 12, 15, 5, 22, 4, 11, 2, 7, 1, 10, 6, 20, 16, 21, 0]
]

# Individual travel costs in the solution
individual_costs = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 347.62]

# Number of depots
depots = {0}

def calculate_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def verify_solution(tours, costs):
    all_visited_cities = set()
    total_cost = 0.0
    for i, tour in enumerate(tours):
        # Requirement 1: Check if the tour starts at a designated depot.
        if tour[0] not in depots:
            print(f"FAIL: Robot {i} does not start at a designated depot.")
            return "FAIL"
        
        # Requirement 2: Visiting each city exactly once check
        for city in tour[1:-1]:
            if city in all_visited_cities:
                print(f"FAIL: City {city} is visited more than once.")
                return "FAIL"
            all_visited_cities.add(city)
        
        # Calculate cost
        calculated_cost = 0
        for j in range(len(tour) - 1):
            calculated_cost += calculate_distance(tour[j], tour[j + 1])
        total_cost += calculated_cost
        
        # Cost verification
        if not np.isclose(calculated_cost, costs[i], atol=0.01):
            print(f"FAIL: Cost mismatch for Robot {i}, expected {costs[i]}, got {calculated_cost}.")
            return "FAIL"

    # Full coverage of cities
    if not all_visited_cities == set(range(len(coordinates))):
        print("FAIL: Not all cities were visited exactly once.")
        return "FAIL"
    
    # Verify the total cost
    if not np.isclose(total_cost, sum(costs), atol=0.01):
        print(f"FAIL: Total cost calculation incorrect, expected {sum(costs)}, got {total_cost}.")
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_solution(robot_tours, individual_costs)
print(result)