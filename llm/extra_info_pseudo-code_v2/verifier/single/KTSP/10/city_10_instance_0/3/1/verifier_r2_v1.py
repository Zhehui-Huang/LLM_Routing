import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_cost_of_tour(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_index_a = tour[i]
        city_index_b = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city_index_a][0], cities[city_index_a][1], 
                                                   cities[city_index_b][0], cities[city_index_b][1])
    return total_cost

# Test Data and Tour Solution
cities = {
    0: (50, 42),  # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

proposed_tour = [0, 6, 3, 9, 0]
proposed_total_cost = 154.96

# Unit Test Function
def test_solution():
    # Test that the tour starts and ends at the depot
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Test that exactly 4 cities are visited (including duplicates at start and end)
    if len(set(proposed_tour) - {0}) != 3:
        return "FAIL"

    # Test that the travel cost is correctly calculated
    calculated_cost = total_cost_of_tour(proposed_tour, cities)
    if abs(calculated_cost - proposed_total_cost) > 1e-2:  # Allowing small floating point discrepancies
        return "FAIL"

    # Test that the solution contains only the intended four cities
    if set(proposed_tour) != {0, 6, 3, 9}:
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution()
print(result)