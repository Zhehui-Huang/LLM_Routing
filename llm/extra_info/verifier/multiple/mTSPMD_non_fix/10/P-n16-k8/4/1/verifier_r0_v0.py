import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Define robots tours (as provided)
robot_tours = {
    0: [3, 8], 1: [1, 10], 2: [2, 7, 6], 3: [4, 11], 4: [0], 5: [5, 14],
    6: [9, 13], 7: [12, 15]
}

# Given results of costs
given_costs = {
    0: 7.81, 1: 7.07, 2: 18.54, 3: 7.21, 4: 0.00, 5: 8.49, 6: 7.21, 7: 6.32
}

# All robots start from city 0
starting_city = 0

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to validate the solution
def validate_solution():
    total_verified_cost = 0.0
    visited_cities = set()

    # Validate each robot's tour
    for robot_id, tour in robot_tours.items():
        prev_city = starting_city
        verified_cost = 0.0
        
        for city in tour:
            verified_cost += calculate_distance(prev_city, city)
            visited_cities.add(city)
            prev_city = city
        
        # Check for tour end condition (not necessary to return to depot in problem statement)
        # Add last trip cost to initial city if returning to the starting depot was needed:
        # verified_cost += calculate_distance(prev_city, starting_city)
        
        # Round to two decimals for comparing with given costs
        verified_cost = round(verified_cost, 2)
        
        if verified_cost != given_costs[robot_id]:
            print(f"FAIL: Robot {robot_id} cost mismatch. Expected {given_costs[robot_id]}, got {verified_cost}")
            return "FAIL"
        
        total_verified_cost += verified_cost
        
    # Check if all cities are visited
    if visited_cities != set(cities.keys()):
        print("FAIL: Not all cities are visited.")
        return "FAIL"
    
    total_given_cost = sum(given_costs.values())
    if round(total_verified_cost, 2) != round(total_given_cost, 2):
        print(f"FAIL: Total cost mismatch. Expected {total_given_cost}, got {total_verified_cost}")
        return "FAIL"
    
    return "CORRECT"

# Run the validation
print(validate_solution())