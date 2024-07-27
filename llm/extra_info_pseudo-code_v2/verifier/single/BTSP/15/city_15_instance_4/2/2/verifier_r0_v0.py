import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost, max_distance_between_cities, cities):
    # Requirement 1: Must visit each city exactly once and must start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Requirement 4: Output the tour as a list of city indices starting and ending at depot city 0
    if not all(isinstance(i, int) for i in tour):
        return "FAIL"
    if len(tour) < 2:
        return "FAIL"
    
    # Calculate total distance and maximum distance between consecutive cities
    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Requirement 2: Travel cost between cities must be the Euclidean distance
    # Requirement 5: Check total travel cost
    if not math.isclose(calculated_total_distance, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 6: Check maximum distance between consecutive cities
    if not math.isclose(calculated_max_distance, max_distance_between_cities, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Define cities positions
cities = [
    (35, 40),  # Depot city 0
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Solution provided
tour = [0, 0]
total_travel_cost = 0.0
max_distance_between_cities = 0.0

# Test the solution
test_result = test_solution(tour, total_travel_cost, max_distance_between_cities, cities)
print(test_result)