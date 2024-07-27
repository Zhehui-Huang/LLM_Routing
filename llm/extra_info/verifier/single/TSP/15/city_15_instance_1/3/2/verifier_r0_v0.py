import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, calculated_cost, cities_coord):
    # Verify tour initiation and termination at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once, depot city twice
    unique_counts = set(tour)
    if len(unique_counts) != len(cities_coord) or tour.count(0) != 2:
        return "FAIL"
    
    # Verify total travel distance
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities_coord[tour[i]], cities_coord[tour[i + 1]])
    
    if abs(total_cost - calculated_cost) > 0.1:  # Allowing minor floating-point discrepancies
        return "FAIL"
    
    return "CORRECT"

# Input data
cities_coord = [
    (29, 51),  # depot city 0
    (49, 20),  # city 1
    (79, 69),  # city 2
    (17, 20),  # city 3
    (18, 61),  # city 4
    (40, 57),  # city 5
    (57, 30),  # city 6
    (36, 12),  # city 7
    (93, 43),  # city 8
    (17, 36),  # city 9
    (4, 60),   # city 10
    (78, 82),  # city 11
    (83, 96),  # city 12
    (60, 50),  # city 13
    (98, 1)    # city 14
]

tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]
total_travel_cost = 355.52  # As provided by user

# Verify the correctness of the given tour solution
result = verify_tour(tour, total_travel_cost, cities_coord)
print(result)