import math

def calculate_distance(point1, point2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tsp_solution(tour, total_cost, cities):
    """ Verify the TSP solution based on the given criteria. """
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once, excluding the depot city
    visited = set(tour) - {0}
    if len(visited) != len(cities) - 1 or any(city not in visited for city in range(1, len(cities))):
        return "FAIL"
    
    # Calculate the total travel cost and compare with the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, calculated_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Given solution to test
tour = [0, 0]
total_cost = 0.0

# Verify the solution
result = verify_tsp_solution(tour, total_cost, cities)
print(result)