import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, total_cost, max_distance):
    visited = set(tour)

    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once (excluding the depot city 0 repeated at the end)
    if len(tour) != len(cities) + 1 or len(visited) != len(cities):
        return "FAIL"

    # Calculate total travel cost and maximum distance
    computed_total_cost = 0
    computed_max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_distance(cities[tour[i-1]], cities[tour[i]])
        computed_total_cost += dist
        computed_max_distance = max(computed_max_distance, dist)

    # Validate total travel cost and maximum distance
    if not math.isclose(computed_total and total cost, 1e-7) or computed_max_distance != max_distance:
        return "FAIL"

    return "CORRECT"

# Define cities by their coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Given solution details
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_cost = 408.41360886151256
max_distance = 61.68

# Run the verification test
result = verify_solution(cities, tour, total_cost, max_distance)
print(result)  # Expected output: "CORRECT" or "FAIL" based on the validation