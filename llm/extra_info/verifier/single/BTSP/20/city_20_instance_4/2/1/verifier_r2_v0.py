import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cities, expected_total_cost, expected_max_distance):
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate the total travel cost and the maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # [Requirement 3] Check the total travel cost and maximum distance
    if not (math.isclose(total_cost, expected_total_data_cost, rel_tol=1e-2) and 
            math.isclose(max_distance, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Define cities based on problem description
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_travel_cost = 410.04
max_distance_between_consecutive_cities = 89.01

# Run tests
result = check_solution(tour, cities, total_travel_cost, max_distance_between_consecutive_cities)
print(result)