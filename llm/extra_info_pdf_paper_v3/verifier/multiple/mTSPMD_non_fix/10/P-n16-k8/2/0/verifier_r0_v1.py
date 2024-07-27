import math
from itertools import chain

# Given data and solution
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}
robot_tours = [
    [0, 13, 8, 0],
    [0, 5, 11, 0],
    [0, 10, 12, 0],
    [0, 1, 4, 0],
    [0, 6, 7, 0],
    [0, 2, 9, 0],
    [0, 15, 14, 0],
    [0, 3, 0]
]
robot_costs = [
    71.62027665741886, 94.25867477710098, 60.8251757953491, 47.577063324685646,
    44.06431012433754, 67.85105818562484, 107.66099338871445, 65.11528238439882
]
overall_cost = 558.9728346376302

# Function to calculate Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Verify each robot route and cost
def verify_robot_routes_and_costs():
    computed_overall_cost = 0
    seen_cities = set()
    
    for tour, reported_cost in zip(robot_tours, robot_costs):
        computed_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            seen_cities.add(city_from)
            computed_cost += calculate_distance(cities_coordinates[city_from], cities_coordinates[city_to])
        
        if not math.isclose(computed_cost, reported_cost, rel_tol=1e-5):
            return "FAIL", "Cost mismatch for a robot"
        computed_overall_cost += computed_cost
        
    seen_cities = seen_cities.union(set(chain.from_iterable(robot_tours)))
    
    if len(seen_cities) != 16:
        return "FAIL", "Not all cities are visited exactly once"
    
    if not math.isclose(computed_overall_cost, overall_cost, rel_tol=1e-5):
        return "FAIL", "Overall cost mismatch"

    return "CORRECT", "All checks passed"

# Calling verification function
result, message = verify_robot_routes_and_costs()
print(result)
print(message)  # Provide more information about the test's outcome.