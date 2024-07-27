import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, coordinates, reported_cost):
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once, except the depot which is visited twice
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(coordinates) - 1 or len(tour) - 1 != len(coordinates):
        return "FAIL"
    
    # Requirement 3: Calculate the total travel distance and compare with reported
    total_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        total_distance += calculate_euclidean_distance(*coordinates[city_a], *coordinates[city_b])
    
    if not math.isclose(total_distance, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
coordinates = [
    (50, 42),  # City 0 (depot)
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Solution details
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
reported_cost = 295.99

# Verify the solution
result = verify_tour(tour, coordinates, reported_cost)
print(result)