import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at the depot city 0."
    
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL: Tour must visit each city exactly once."
    
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return f"FAIL: Total cost should be {calculated_cost}, but got {total_cost}."

    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return f"FAIL: Max distance should be {calculated_max_distance}, but got {max_distance}."

    return "CORRECT"

# Coordinates of each city, with the depot city as the first element
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63),
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# The solution provided
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_travel_cost = 610.59
max_distance = math.inf  # "inf" indicates an unrealistic value for max distance

# Check the solution
result = verify_solution(tour, total_travel_cost, max_distance, cities)
print(result)