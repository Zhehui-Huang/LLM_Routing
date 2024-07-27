import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, distances, requirement_details):
    # Extract details from requirement details
    start_city, must_visit_all_cities_once, minimize_max_consecutive_distance, heuristic_algorithm_used, total_travel_cost, max_consecutive_distance = requirement_details
    
    # Requirement 1: Check start and end city
    if tour[0] != start_city or tour[-1] != start_city:
        return "FAIL"
    
    # Requirement 2: Check all cities are visited exactly once (ignoring start/end depot which appears twice)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) + 1 != len(tour) - 1 or any(tour.count(city) > 1 for city in unique_cities):
        return "FAIL"
    
    # Requirement 5: Tour should start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 6: Check computed total cost
    computed_total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if not math.isclose(computed_total_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 7: Check maximum distance between consecutive cities
    max_tour_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if not math.isclose(max_tour_distance, max_consecutive_distance, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 3 & 4 are inherently subjective and based on previous requirements, but must be checked in functionally present code
    return "CORRECT"

# Provided solution details
tour_solution = [8, 17, 8, 8]
total_travel_cost_solution = 12.81
max_distance_solution = 6.40

# Define the cities relations based on provided example
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate distances
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Requirement details
requirement_details = (
    0,  # Start city
    True,  # Must visit all cities exactly once (logic check)
    True,  # Minimize maximum consecutive distance
    True,  # Heuristic algorithm must be used
    total_travel_cost_solution,
    max_distance_solution
)

# Check the solution
test_result = verify_solution(tour_solution, distances, requirement_messages)
print(test_result)