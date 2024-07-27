import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, expected_total_cost):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all other cities are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 14 or any(i not in visited_cities for i in range(1, 15)):
        return "FAIL"

    # Calculate the total cost and compare with expected total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost, expected_total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Coordinates of cities with depot at index 0
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Provided solution
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.57

# Check the solution
result = verify_solution(tour, cities, total_travel_code)
print(result)