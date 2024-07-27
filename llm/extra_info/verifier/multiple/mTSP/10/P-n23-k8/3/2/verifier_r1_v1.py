import math

# Coordinates of Cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot tours and costs
robot_tours = [
    [0, 10, 12, 15, 3, 0], [0, 16, 1, 6, 0], [0, 7, 22, 17, 9, 0],
    [0, 18, 19, 0], [0, 2, 13, 8, 0], [0, 21, 0], [0, 4, 11, 0], [0, 20, 5, 14, 0]
]

provided_costs = [85.55, 40.21, 75.20, 89.42, 72.58, 4.47, 57.39, 62.45]
reported_total_cost = 487.28

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_solution(tours, costs, reported_total_cost):
    visited_cities = set()
    calculated_total_cost = 0
    
    if len(tours) != 8:  # There should be 8 robots
        return "FAIL"
    
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:  # Tour must start and end at the depot
            return "FAIL"
        
        # Calculate tour cost
        tour_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if abs(tour_cost - costs[robot_id]) > 1e-2:  # Verify cost with a tolerance for float precision issues
            return "FAIL"
        calculated_total_cost += tour_cost
        
        visited_cities.update(tour[1:-1])  # Add cities visited, excluding the depot
    
    if len(visited_cities) != 22 or any(city not in visited_cities for city in range(1, 23)):  # Each city should be visited once
        return "FAIL"
    
    # Check reported total cost
    if abs(calculated_total_cost - reported_total_cost) > 1e-2:
        return "FAIL"
    
    return "CORRECT"

# Run the verification
test_result = verify_solution(robot_tours, provided_costs, reported_total_reported)
print(test_result)