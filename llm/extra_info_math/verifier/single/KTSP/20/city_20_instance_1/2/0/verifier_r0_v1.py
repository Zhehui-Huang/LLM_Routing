import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, coordinates, expected_cost):
    # Requirement 1: Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if the tour visits exactly 7 cities, including depot city
    if len(set(tour)) != 7 or len(tour) != 8:
        return "FAIL"
    
    # Requirement 3: Check if the travel cost is computed correctly using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city_idx1, city_idx2 = tour[i], tour[i + 1]
        total_cost += euclidean_distance(coordinates[city_idx1], coordinates[city_idx2])

    if not math.isclose(total_cost, expected_cost, abs_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Define city coordinates (index corresponds to city number, 0 indexed)
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Define the tour and expected total travel cost
tour = [0, 6, 2, 13, 8, 9, 14, 0]
expected_cost = 130.6658168109853

# Perform the validation
result = validate_tour(tour, coordinates, expected_cost)
print(result)