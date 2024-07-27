import numpy as np
from scipy.spatial.distance import euclidean

# Constants defining the environment
cities_coordinates = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

# Provided solution details
tour = [0, 19, 8, 17, 18, 10, 15, 0]
provided_total_cost = 214.05369692369052

def verify_tour(tour, cities_coordinates, provided_total_cost):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Create a set of visited cities to ensure each city is visited once
    visited_cities = set(tour)
    
    # Check for duplicate visits and if all cities are visited
    if len(visited_cities) != len(tour) - 1 or len(visited_cities) != len(cities_coordinates):
        return "FAIL"
    
    # Calculate the total travel cost of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += euclidean(cities_coordinates[city_a], cities_coordinates[city_b])

    # Compare calculated cost with the provided cost
    if not np.isclose(calculated_cost, provided_total_cost, atol=1e-6):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_tour(tour, cities_coordinates, provided_total_cost)
print(result)