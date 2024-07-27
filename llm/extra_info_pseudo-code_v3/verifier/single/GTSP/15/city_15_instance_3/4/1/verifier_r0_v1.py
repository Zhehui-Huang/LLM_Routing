import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost):
    # City coordinates
    coordinates = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73),
        (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30),
        (70, 95), (29, 64), (32, 79)
    ]
    
    # City groups
    city_groups = [
        [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
    ]

    # Verify city count
    if len(coordinates) != 15:
        return "FAIL: Incorrect number of cities"

    # Verify depot starting/ending
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start or end at the depot"

    # Check if one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour:
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups[i] += 1
    
    if not all(x == 1 for x in visited_groups):
        return "FAIL: Not exactly one city from each group is visited"

    # Check travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return f"FAIL: Incorrect total travel cost, expected close to {total_travel_step}, got {total_travel_cost}"

    return "CORRECT"

# Example Solution
tour_example = [0, 14, 5, 10, 11, 8, 9, 0]
total_travel_cost_example = 166.76

# Run Test
result = test_solution(tour_example, total_travel_cost_example)
print(result)