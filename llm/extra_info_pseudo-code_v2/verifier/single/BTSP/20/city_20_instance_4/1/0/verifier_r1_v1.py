import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, distances, requirement_details):
    start_city, total_travel_cost, max_distance = requirement_details
    
    # Requirement 1: The robot must start and end at depot city 0.
    if tour[0] != start_city or tour[-1] != start_city:
        return "FAIL"
    
    # Requirement 2: The robot must visit each city exactly once.
    visited = set(tour[1:-1])
    if len(visited) + 1 != len(tour) - 1 or any(tour.count(city) > 1 for city in visited):
        return "FAIL"

    # Requirement 5: Output must include the tour path as a list of city indices starting and ending at city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 6: Output must include the total travel cost of the tour.
    computed_total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if not math.isclose(computed_total_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    # Requirement 7: Output must include the maximum distance between any two consecutive cities in the tour.
    max_tour_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if not math.isclose(max_tour_distance, max_distance, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details from execution output
tour_solution = [8, 17, 8, 8]
total_travel_cost_solution = 12.81
max_distance_solution = 6.40

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Prepare distances matrix
distances = {i: {j: calculate_distance(cities[i], cities[j]) for j in cities} for i in cities}

# Requirement details to match with provided solution
requirement_details = (0, total_travel_cost_solution, max_distance_solution)

# Check the solution
test_result = verify_solution(tour_solution, distances, requirement_details)
print(test_result)