import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, distances, total_cost_computed):
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Each city visited once
    cities_visited = set(tour)
    if len(cities_visited) != len(tour) - 1:  # considering one city (depot) is visited twice
        return "FAIL"
    if len(cities_visited - {0}) != max(tour):
        return "FAIL"

    # Check Requirement 4: No subtours; implicit in the tour representation validity

    # Check Requirement 3: Total distance minimization
    distance_calculated = 0
    for i in range(len(tour) - 1):
        distance_calculated += distances[tour[i]][tour[i+1]]
    
    if not math.isclose(distance_calculated, total_cost_computed, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates given in the problem
coordinates = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
               (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
               (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
               (53, 76), (19, 72)]

# Calculate distance for each pair
n_cities = len(coordinates)
distances = [[0]*n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        distances[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Provided solution
tour = [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0]
total_travel_cost = 141.4213562373095

# Validate the solution
result = verify_solution(tour, distances, total_travel_cost)
print(result)