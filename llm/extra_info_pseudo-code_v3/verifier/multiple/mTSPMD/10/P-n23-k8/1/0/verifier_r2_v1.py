import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours and costs provided
robots_tours = {
    0: ([0, 19, 22, 0], 102.86),
    1: ([1, 14, 15, 1], 96.61),
    2: ([2, 17, 20, 2], 50.68),
    3: ([3, 18, 9, 3], 55.22),
    4: ([4, 10, 21, 4], 55.70),
    5: ([5, 16, 8, 5], 67.07),
    6: ([6, 11, 13, 6], 85.24),
    7: ([7, 12, 7], 55.03)
}

# Function to calculate Euclidean distance
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Verification function
def verify_solution(tours, city_coordinates):
    visited_cities = set()
    total_calculated_cost = 0.0
    for robot, (tour, reported_cost) in tours.items():
        # Starting and ending at depot
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"
        
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coordinates[tour[i]], city_pressure[tour[i+1]])
            visited_cities.add(tour[i])
        
        # Add the last city because it's visited.
        visited_cities.add(tour[-1])

        # Verify cost correctness within a reasonable precision
        if not math.isclose(tour_cost, reported_cost, abs_tol=1e-2):
            return "FAIL"
        
        total_calculated_cost += tour_cost

    # Check if all cities visited exactly once
    if visited_cities != set(city_coordinates.keys()):
        return "FAIL"
    
    return "CORRECT"

# Use the verification function
result = verify_solution(robots_tours, cities)
print(result)