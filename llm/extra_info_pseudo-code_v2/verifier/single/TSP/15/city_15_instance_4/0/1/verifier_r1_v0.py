import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, expected_cost, city_coordinates):
    # [Requirement 1] Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city besides the depot must appear exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(city_coordinates) - 1 or any(v not in visited_cities for v in range(1, len(city_coordinates))):
        return "FAIL"
    
    # [Requirement 3] Calculate the actual cost and compare with the given cost
    actual_cost = 0
    for i in range(1, len(tour)):
        actual_cost += euclidean_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    
    if not math.isclose(actual_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates according to the problem definition
city_coordinates = [
    (35, 40),  # City 0 - Depot
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39),  # City 14
]

# Provided tour and cost
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.8447016788252

# Validate the tour and output the result
result = verify_tour(tour, total_travel_cost, city_coordinates)
print(result)