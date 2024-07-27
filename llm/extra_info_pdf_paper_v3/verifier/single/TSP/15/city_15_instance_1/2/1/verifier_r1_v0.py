import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_cost, city_coordinates):
    # Check if tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    visited_cities = tour[1:-1]  # Excluding the start/end depot city
    if len(set(visited_cities)) != len(visited_cities) or len(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Check if the total cost matches the accumulated travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a_idx = tour[i]
        city_b_idx = tour[i + 1]
        city_a = city_coordinates[city_a_idx]
        city_b = city_coordinates[city_b_idx]
        calculated_cost += euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given coordinates (this should come from actual problem data in practice)
city_coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1),
]

# Given solution to verify
tour = [0, 10, 4, 0, 9, 3, 7, 1, 6, 13, 2, 12, 11, 8, 14, 5, 0]
total_cost = 405.85672628610496

# Verification
result = verify_tour(tour, total_cost, city_coordinates)
print(result)