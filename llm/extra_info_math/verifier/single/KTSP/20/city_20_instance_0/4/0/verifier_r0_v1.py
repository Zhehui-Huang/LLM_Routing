import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # Coordinates of cities
    city_coords = [
        (8, 11),  # City 0: Depot
        (40, 6),  # City 1
        (95, 33),  # City 2
        (80, 60),  # City 3
        (25, 18),  # City 4
        (67, 23),  # City 5
        (97, 32),  # City 6
        (25, 71),  # City 7
        (61, 16),  # City 8
        (27, 91),  # City 9
        (91, 46),  # City 10
        (40, 87),  # City 11
        (20, 97),  # City 12
        (61, 25),  # City 13
        (5, 59),  # City 14
        (62, 88),  # City 15
        (13, 43),  # City 16
        (61, 28)   # City 17
    ]
    
    # Requirement 1: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 4 cities, including the depot
    unique_cities = set(tour[:-1])  # Excluding the last element which is the same as the first
    if len(unique_cities) != 4:
        return "FAIL"
    
    # Calculate the actual travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    
    # Requirement 3: Minimizing the cost -> Check if costs match (using small tolerance for float comparisons)
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define the solution to test
tour_test = [0, 17, 13, 4, 0]
total_cost_test = 58.06

# Test the given solution
result = verify_solution(tour_test, total_cost_test)
print(result)