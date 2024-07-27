import math

# Define the cities by their coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
          (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Given tour and cost
given_tour = [0, 1, 4, 12, 3, 7, 2, 11, 8, 6, 13, 10, 9, 5, 14, 0]
given_cost = 303.3094531921133

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def check_tour():
    # Verify start and end at the depot (Requirement 1)
    if given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once, excluding depot city (Requirement 2)
    visited_cities = set(given_tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Verify the cost calculation (Requirement 3)
    calculated_cost = 0
    for i in range(len(given_tour) - 1):
        calculated_cost += euclidean_distance(cities[given_tour[i]], cities[given_tour[i+1]])
    if not math.isclose(calculated_cost, given_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Check and print the result of the check
print(check_tour())