import math

# Given city coordinates with their IDs as indexes
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define robots tours
robots_tours = {
    0: [0, 21, 16, 0],
    1: [1, 1],
    2: [2, 13, 2],
    3: [3, 3],
    4: [4, 11, 15, 12, 4],
    5: [5, 22, 5],
    6: [6, 16, 6],
    7: [7, 22, 7]
}

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities based on their coordinates."""
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def check_tour_requirements(robots_tours):
    """Check the solution against the defined requirements."""
    visited_cities = set()
    total_cost = 0
    
    for robot_id, tour in robots_tours.items():
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL: Start or end depot is incorrect for robot {}".format(robot_id)
        
        previous_city = tour[0]
        for city in tour[1:]:
            if city in visited_cities and city != tour[0]:
                return "FAIL: City {} visited more than once".format(city)
            visited_cities.add(city)
            total_cost += calculate_distance(previous_city, city)
            previous_city = city

    # Check if all cities are visited exactly once, excluding depot cities.
    if len(visited_cities) != len(cities):
        return "FAIL: Not all cities were visited"

    # If all checks pass, return correct and the calculated total cost
    return "CORRECT", total_cost

# Running the unit test
test_result = check_tour_requirements(robots_tours)
if isinstance(test_result, str):
    print(test_result)
else:
    print(test_result[0])  # CORRECT or FAIL
    print("Overall Total Travel Cost: {:.2f}".format(test_result[1]))