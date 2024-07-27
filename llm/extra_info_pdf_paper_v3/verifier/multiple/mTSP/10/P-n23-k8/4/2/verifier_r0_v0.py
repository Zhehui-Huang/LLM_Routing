import numpy as np

def euclidean_distance(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def verify_tours(robots_tours, cities_coordinates):
    # Total number of unique cities visited (excluding the depot multiple times)
    unique_cities_visited = set()
    all_visited = []

    for tour in robots_tours:
        # Requirement 2: Tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Collect cities visited by all robots
        all_visited.extend(tour[1:-1])  # exclude the depot city ending and starting
        
        # Collect unique cities in this tour excluding starting and ending depot city
        unique_cities_visited.update(tour[1:-1])
    
    # Requirement 1, 4: All cities should be visited once exactly excluding the depot as a destination
    if len(unique_cities_visited) != len(cities_coordinates) - 1:
        return "FAIL"

    # Check if all cities except the depot were visited exactly once
    if sorted(all_visited) != sorted(range(1, len(cities_coordinates))):
        return "FAIL"

    # Compute the total travel costs and check with given costs
    total_cost_computed = 0
    for tour in robots_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        total_cost_computed += tour_cost
    
    # Requirement 3: Check if the total cost is approximately equal to given total cost (consider floating point precision)
    if not np.isclose(total_cost_computed, 637.8813250870519, rtol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Tours and costs for each robot
robots_tours = [
    [0, 7, 3, 11, 0], 
    [0, 6, 13, 1, 0], 
    [0, 5, 10, 4, 0],
    [0, 8, 14, 20, 0], 
    [0, 9, 17, 22, 0], 
    [0, 12, 2, 21, 0], 
    [0, 18, 19, 0], 
    [0, 15, 16, 0]
]

# Verification
result = verify_tours(robots_tours, cities_coordinates)
print(result)