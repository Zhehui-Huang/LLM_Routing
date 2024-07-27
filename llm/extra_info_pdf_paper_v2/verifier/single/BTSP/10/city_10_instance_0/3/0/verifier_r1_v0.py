import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tsp_solution(tour, positions, expected_max_distance, total_cost):
    # Check if the tour starts and ends at the depot (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (Requirement 1)
    if len(set(tour)) != len(positions) or sorted(set(tour)) != sorted(tour[:-1]):
        return "FAIL"

    # Calculate travel cost and maximum distance (Requirement 2 and 3)
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        dist = calculate_euclidean_distance(positions[city1][0], positions[city1][1], positions[city2][0], positions[city2][1])
        calculated_total_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)

    # Check if total travel cost and max distance are correctly calculated or not
    if abs(calculated_total_cost - total_cost) > 1e-5 or abs(calculated_max_distance - expected_max_distance) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Test data
positions = [
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

tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
total_travel_cost = 328.3966856465968
max_distance = 45.18849411078001

# Execute test
result = test_tsp_solution(tour, positions, max_distance, total_travel_cost)
print(result)