import numpy as np

# Coordinates for cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
    (83, 96), (60, 50), (98, 1)
]

# Calculated tour from the solver
tour = [0, 4, 5, 6, 7, 3, 10, 9, 1, 13, 11, 12, 2, 8, 14, 0]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify that the tour starts and ends at the depot city 0
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Verify that each city is visited exactly once
def check_all_visited_once(tour):
    return sorted(tour[:-1]) == list(range(len(cities)))

# Calculate the maximum distance between any two consecutive cities in the tour
def maximum_distance_in_tour(tour):
    max_dist = 0
    for i in range(len(tour) - 1):
        max_dist = max(max_dist, distance(tour[i], tour[i + 1]))
    return max_dist

# Correctly reported maximum distance
reported_max_distance = 85.21150157109074

# Test the solution
def test_solution(tour, reported_max_distance):
    if not check_start_end(tour):
        return "FAIL - Tour does not start and end at depot"
    if not check_all_visited_once(tour):
        return "FAIL - Not all cities are visited exactly once"
    max_dist = maximum_distance_in_tour(tour)
    if np.isclose(max_dist, reported_max_distance, atol=0.001):
        return "CORRECT"
    else:
   	    return f"FAIL - Mismatch in maximum distance calculated: {max_dist} vs reported: {reported_max_distance}"

# Running the test
result = test_solution(tour, reported_max_distance)
print(result)