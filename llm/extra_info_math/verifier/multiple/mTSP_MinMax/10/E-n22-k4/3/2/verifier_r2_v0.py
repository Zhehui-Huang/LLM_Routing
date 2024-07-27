import math

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Provided tours and their costs
robot_tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 14, 16, 19, 21, 17, 20, 18, 15, 12, 10, 8, 6, 9, 7, 5, 2, 1, 3, 4, 11, 13, 0]
]
costs = [0, 0, 0, 288]

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check the requirements
def verify_solution(robot_tours, costs):
    all_visited = set()
    total_cities = set(range(1, 22))

    for tour in robot_tours:
        # Check Each robot must leave the depot exactly once and return
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check Each city is visited exactly once by one robot
        visited = set(tour[1:-1])  # Exclude the starting and ending depot
        if not visited.isdisjoint(all_visited):  # No city should be revisited
            return "FAIL"
        all_visited.update(visited)
        
        # Check Flow conservation constraints, subtours, and binary constraints
        for idx in range(1, len(tour) - 1):
            if tour[idx] == tour[idx + 1]:  # Binary constraints: no repeats
                return "FAIL"
        
        # Check continuous constraints (basic check: all indices should be valid cities)
        for city in tour[1:-1]:
            if city not in total_cities:
                return "FAIL"

    # After looping through all robots
    if all_visited != total_cities:
        return "FAIL"  # Not all cities were visited

    return "CORRECT"

# Print the result
print(verify_solution(robot_tours, costs))