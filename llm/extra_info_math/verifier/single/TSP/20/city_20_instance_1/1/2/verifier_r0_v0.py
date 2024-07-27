import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    # Check if starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited_cities = set(tour[1:-1])  # Excluding the depot city which should be visited twice (start, end)
    if len(visited_cities) != len(cities) - 1:
        return "FAIL"
    
    # Check if all cities in tour are in the available city list
    if not all(city in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Calculate the total distance of the provided tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Approximate computation to avoid mismatches due to floating point precision
    expected_distance = 376.93
    if not math.isclose(total_distance, expected_distance, abs_tol=1.0):
        return "FAIL"
    
    return "CORRECT"

# City coordinates with the depot as city 0
city_coords = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Tour solution to be verified
tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 16, 11, 10, 4, 7, 5, 14, 3, 0]

# Verify the tour
verification_result = verify_tour(tour, city_coords)
print(verification_result)