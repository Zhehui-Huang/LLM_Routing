import math

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided robot tours and costs
robot_tours = [
    [0, 21, 7, 9, 0],     # Robot 0
    [0, 16, 5, 17, 0],    # Robot 1
    [0, 6, 22, 8, 0],     # Robot 2
    [0, 1, 12, 15, 0],    # Robot 3
    [0, 20, 14, 18, 0],   # Robot 4
    [0, 10, 3, 19, 0],    # Robot 5
    [0, 2, 13, 0],        # Robot 6
    [0, 4, 11, 0]         # Robot 7
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the specified travel costs and check correctness
def verify_solution(robot_tours, cities, max_allowed_cost):
    all_visited_cities = set()
    
    for tour in robot_towers:
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate travel cost for current tour
        travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Compare calculated travel cost with provided data
        if abs(provided_costs[index] - travel_cost) > 1e-5:  # Allow some floating-point leeway
            return "FAIL"
        
        all_visited_cities.update(tour)

    # Check if all cities visited exactly once excluding the depot (city 0)
    if all_visited_cities != set(cities.keys()):
        return "FAIL"
    
    # Check the maximum travel cost
    if max(provided_costs) > max_allowed_cost:
        return "FAIL"

    return "CORRECT"

# Travel costs from solution
provided_costs = [
    64.44813392462525, 69.8854703386842, 80.07557187815789,
    66.20536151154266, 106.70538736634138, 89.03001890899068, 
    59.19962073688813, 57.394073777130664
]

# Validate the solution
result = verify_solution(robot_tours, cities, 106.70538736634138)
print(result)