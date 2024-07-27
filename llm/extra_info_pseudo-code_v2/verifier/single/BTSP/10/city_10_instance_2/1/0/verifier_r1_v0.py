import math

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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Provided solution
solution_tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
reported_total_cost = 418.32
reported_max_distance = 69.43

# Validate the solution
def validate_tour(tour, reported_cost, reported_max_dist):
    # [Requirement 3] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Check if each city is visited exactly once (except the depot)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(tour[:-1]) != set(cities.keys()):
        return "FAIL"
    
    # Calculate total cost and max distance
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += dist
        max_distance = max(max_distance, dist)
    
    # [Requirement 4] Check total travel cost
    if not math.isclose(total_travel_image_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    # [Requirement 5] Check maximum distance between consecutive cities
    if not math.isclose(max_distance, reported_max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
validation_result = validate_tour(solution_tour, reported_total_cost, reported_max_distance)
print(validation_result)