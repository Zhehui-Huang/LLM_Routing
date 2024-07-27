import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_travel_cost):
    # Unpacking city coordinates from index
    city_coords = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
        (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
        (83, 96), (60, 50), (98, 1)
    ]

    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except depot
    visited = set(tour)
    if len(tour) != len(cities) + 1 or len(visited) != len(cities) or visited != set(cities):
        return "FAIL"

    # Calculate the cost from the tour provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])

    # Check if the calculated cost matches the total_travel_cost
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Given Solution
cities = list(range(15))
tour = [0, 10, 4, 9, 3, 7, 1, 6, 13, 2, 12, 11, 8, 14, 5, 0]
total_travel_cost = 396.8

# Run the verification test
test_result = verify_solution(cities, tour, total_travel_msot)
print(test_result)  # Output result