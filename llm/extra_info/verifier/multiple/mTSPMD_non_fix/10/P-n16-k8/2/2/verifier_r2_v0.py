import math

# List all cities (0 to 15)
all_cities = set(range(16))

# Define the tours and respective coordinates
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

# List to hold all visited cities from the tours
visited_cities = set()

# Check requirement 1: All cities visited exactly once
for tour in tours.values():
    visited_cities.update(tour)

# Verify all cities are covered and there are no unvisited cities
all_cities_visited = visited_cities == all_cities

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Verify that all robots start their tours from depot city 0
all_start_from_depot = all(tour[0] == 0 for tour in tours.values())

# Calculate total travel costs
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours.values():
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_cost += cost
    return total_cost

# Expected and actual total travel costs
expected_total_cost = 216.22707966298873
actual_total_cost = calculate_total_cost(tours)

# Check Requirements 4, 5, 6 (check within tolerance)
cost_within_tolerance = math.isclose(actual_total_cost, expected_total_test, rel_tol=1e-9)

# Overall outcome
if all_cities_visited and all_start_from_depot and cost_within_tolerance:
    print("CORRECT")
else:
    print("FAIL")