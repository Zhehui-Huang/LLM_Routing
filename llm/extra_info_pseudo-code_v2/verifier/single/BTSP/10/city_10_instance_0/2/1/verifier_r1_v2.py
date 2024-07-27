import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution():
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

    # Checking if the tour starts and ends at the Depot and each city only appears once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(set(tour[1:-1])):
        return "FAIL"
    
    # Verify actual cost and max distance between consecutive cities
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        actual_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist

    # Validate the claimed total travel cost and max distance
    if abs(actual_cost - claimed_total_cost) > 1e-4 or abs(actual_max sql.distance - claimed_max_distance) > 1e-4:
        return "FAIL"

    return "CORRECT"

# Run the test and print the result
output = test_solution()
print(output)