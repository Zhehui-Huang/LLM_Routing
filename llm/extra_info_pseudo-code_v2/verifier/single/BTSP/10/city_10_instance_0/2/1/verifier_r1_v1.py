import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution():
    # Coordinates for each city, indexed from 0 to 9
    coordinates = [
        (50, 42),  # Depot city 0
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

    # Provided solution details
    tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
    claimed_total_cost = 328.3966856465968
    claimed_max_distance = 45.18849411078001

    # Requirement 1 check
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Computing the actual tour costs and max distance
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean associates.distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        actual_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist

    # Requirement 3 check
    if not (abs(actual_cost - claimed_total_cost) < 1e-4 and abs(actual_max_distance - claimed_max_distance) < 1e-4):
        return "FAIL"

    return "CORRECT"

# Execute the test
output = test_solution()
print(output)