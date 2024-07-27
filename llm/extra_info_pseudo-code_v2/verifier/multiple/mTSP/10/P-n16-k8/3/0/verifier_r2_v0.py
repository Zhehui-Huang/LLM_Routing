import math

# City coordinates, including the depot city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot tours given in the task output
robot_tours = [
    [0, 1, 9, 0], [0, 10, 2, 0], [0, 11, 3, 0], [0, 4, 12, 0],
    [0, 5, 13, 0], [0, 6, 14, 0], [0, 7, 15, 0], [0, 8, 0]
]

# Expected individual robot costs
expected_costs = [72.88, 52.46, 86.04, 64.99, 68.36, 64.17, 83.62, 64.90]

def calculate_euclidean_distance(pt1, pt2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def test_robot_tours():
    # Check for unique city visits excluding depot
    visited_cities = set()
    total_cost = 0

    for i, tour in enumerate(robot_tours):
        # Check start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Add cities to visited set and compute travel cost
        tour_cost = 0
        for j in range(1, len(tour)):
            city_from = tour[j - 1]
            city_to = tour[j]
            tour_cost += calculate_euclidean_distance(cities[city_from], cities[city_to])
            if city_to != 0:  # Avoid adding the depot city to visits
                visited_cities.add(city_to)
        
        # Check computed tour cost against expected rounded to 2 decimals
        if round(tour_cost, 2) != expected_costs[i]:
            return "FAIL"
        
        total_cost += tour_cost
    
    # Check if all cities have been visited exactly once
    if len(visited_cities) != 15 or visited_cities != set(range(1, 16)):
        return "FAIL"

    # Check total overall cost rounding error threshold
    if round(total_cost, 2) != 557.42:
        return "FAIL"
    
    return "CORRECT"

# Perform the unit test
print(test_robot_tours())