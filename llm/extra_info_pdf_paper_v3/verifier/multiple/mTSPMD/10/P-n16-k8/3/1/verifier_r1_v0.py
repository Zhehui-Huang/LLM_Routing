import math

# Define the city coordinates as specified
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours provided by the solution
tours = [
    [0, 14, 0], [1, 11, 1], [2, 9, 2], [3, 10, 3],
    [4, 15, 4], [5, 12, 5], [6, 8, 6], [7, 13, 7]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Verify if each robot starts and ends at the correct depot
def robot_starts_ends_correctly():
    for robot_id, tour in enumerate(tours):
        if not (tour[0] == robot_id and tour[-1] == robot_id):
            return False
    return True

# Check if all cities are visited exactly once
def all_cities_visited_once():
    visited = set()
    for tour in tours:
        for city in tour[1:-1]: 
            if city in visited:
                return False
            visited.add(city)
    # Check that all non-depot cities are visited
    if len(visited) != 8:
        return False
    return True

# Calculate costs and verify they match reported costs
def verify_travel_costs():
    reported_costs = [61.741396161732524, 37.73592452822641, 29.5296461204668, 24.413111231467404,
                      18.439088914585774, 70.3420215802759, 45.34313619501854, 18.439088914585774]
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(tour[i], tour[i + 1])
        calculated_costs.append(cost)
    
    for reported, calculated in zip(reported_costs, calculated_costs):
        if not math.isclose(reported, calculated, abs_tol=0.001):
            return False
    return True

# Verify all aspects of the solution
def test_solution():
    if not robot_starts_ends_correctly():
        return "FAIL"
    if not all_cities_visited_once():
        return "FAIL"
    if not verify_travel_costs():
        return "FAIL"
    return "CORRECT"

# Run the test
result = test_overall_solution()
print(result)