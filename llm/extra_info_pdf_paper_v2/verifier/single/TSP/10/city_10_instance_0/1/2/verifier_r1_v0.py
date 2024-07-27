import numpy as np

# Provided solution details
tour = [0, 0, 5, 7, 6, 1, 2, 9, 4, 8, 3]
total_cost = 229.98439854515925

# City coordinates as provided in the task earlier
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def validate_tour(tour, cities, total_cost):
    # [Requirement 1] Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit all cities exactly once, except the depot
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1:
        return "FAIL"
    
    # [Requirement 4] The tour listed is starting and ending at the depot
    if tour.count(0) != 2:  # Ensure only start and end at depot
        return "FAIL"

    # [Requirement 3 & 5] Calculate total travel cost and match
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        
    if not np.isclose(calculated_cost, total_cost, atol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Execute the validation function
result = validate_tour(tour, cities, total_cost)
print(result)