import math

# List all cities (0 to 15)
all_cities = set(range(16))

# Define tours and respective coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Given tours
tours = {
    0: [0, 5, 14],
    1: [0, 15, 12],
    2: [0, 2, 7, 13, 9],
    3: [0],
    4: [0, 4, 11],
    5: [0, 6],
    6: [0, 1, 10],
    7: [0, 8, 3]
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate total travel costs and check city visits
def test_solution():
    visited_cities = set()
    total_calculated_cost = 0

    for key, tour in tours.items():
        if not tour or tour[0] != 0:
            return "FAIL"
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            visited_cities.add(start_city)
            total_calculated_cost += calculate_distance(city_coordinates[start_city], city_coordinates[end_city])
        visited_cities.add(tour[-1])  # Add last city in tour
    
    # Requirement 1: All cities must be visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Requirement 5 & 6: Minimum cost calculation within tolerance
    expected_total_cost = 216.22707966298873  # Total cost reported
    if not math.isclose(total_calculated_cost, expected_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution()
print(result)