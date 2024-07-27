import math

# Coordinates of the cities
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((coordinates[city_a][0] - coordinates[city_b][0]) ** 2 + (coordinates[city_a][1] - coordinates[city_b][1]) ** 2)

# Provided solution tour and its reported metrics
solution_tour = [0, 14, 5, 7, 4, 16, 10, 11, 3, 6, 2, 13, 12, 8, 15, 19, 18, 17, 1, 9, 0]
reported_total_travel_cost = 516.43
reported_max_distance = 85.33

# Validate the tour
def validate_tour(tour, expected_total_cost, expected_max_distance):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    unique_cities = set(tour)
    if len(unique_cities) != 21 or len(tour) != 21:  # 20 cities + 1 to include starting city twice
        return "FAIL"
    
    # Calculate total travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Requirement 3: Check reported values
    if not (math.isclose(total_cost, expected_total_cost, rel_tol=1e-2) and 
            math.isclose(max_distance, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
result = validate_tour(solution_tour, reported_total_travel_cost, reported_max_distance)
print(result)