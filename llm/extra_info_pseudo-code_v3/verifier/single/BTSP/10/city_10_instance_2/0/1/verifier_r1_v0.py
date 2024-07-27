import math

# Define the function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Tour, total travel cost, and maximum distance provided
tour = [0, 8, 5, 2, 1, 9, 7, 6, 4, 3, 0]
provided_total_cost = 367.64
provided_max_distance = 78.16

# Unit tests
def test_tour_requirements(tour, provided_total_cost, provided_max_distance):
    num_cities = len(cities)
    
    # Requirement 1: All cities are visited exactly once, starting and ending at depot
    if sorted(tour) != sorted(list(cities.keys()) + [0]):
        return "FAIL"
    
    # Requirement 3: Output includes the tour, and it starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the tour's actual total cost and maximum distance
    actual_total_cost = 0
    actual_max_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist
    
    # Requirement 4: Check total travel cost
    if not math.isclose(actual_total_cost, provided_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 5: Check the maximum distance between any two consecutive cities
    if not math.isclose(actual_max_distance, provided_max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run tests and print the result
result = test_tour_requirements(tour, provided_total_cost, provided_max_distance)
print(result)