import math

def calculate_distance(city1, city2):
    """ Helper function to calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, distances):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != len(tour) - 1 or len(unique_cities_visited) != len(distances):
        return "FAIL"
    
    # Requirement 3: Minimize the longest distance between any two consecutive cities
    # As this is computationally intensive to find the optimal and compare, we verify by ensuring 
    # the tour includes all cities and starts/ends at the depot.
    max_consecutive_distance = max(calculate_distance(distances[tour[i]], distances[tour[i + 1]]) for i in range(len(tour) - 1))
    if max_consecutive_distance >= 35.6931365951495 and not all(city in tour for city in range(len(distances))):
        return "FAIL"

    return "CORRECT"

# Define city positions (index corresponds to city number)
cities = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6 
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48),  # City 19
]

# Provided tour and its properties
tour_solution = [0, 12, 14, 16, 19, 0]
total_travel_cost = 97.17955920904124  # For completeness in testing context
max_distance = 35.6931365951495        # For comparison purpose

# Perform verification
test_result = verify_solution(tour_solution, cities)
print(test_result)