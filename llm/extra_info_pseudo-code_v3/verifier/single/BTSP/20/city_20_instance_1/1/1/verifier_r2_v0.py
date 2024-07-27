import math

# Given the tour and other output values
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 6, 2, 9, 13, 8, 1, 15, 18, 17, 19, 12, 0]
total_travel_cost = 503.93280249020313
maximum_consecutive_distance = 96.1041102138717

# Coordinates as provided in the description
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def unit_tests(tour, total_travel_cost, maximum_consecutive_distance):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (excluding the start/end city)
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Check if the computed total travel cost is correct
    computed_total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Check if the maximum distance between consecutive cities is computed correctly
    computed_max_distance = max(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(computed_max_distance, maximum_consecutive_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the unit tests
output = unit_tests(tour, total_travel_cost, maximum_consecutive_distance)
print(output)