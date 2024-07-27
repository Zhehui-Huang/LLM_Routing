import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates based on the problem statement
    city_positions = {
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
    
    # Checking the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking the tour visits exactly 6 cities including depot city
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Check if all tour cities are valid and from the set
    if not all(city in city_positions for city in tour):
        return "FAIL"
    
    # Verify the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += compute_euclidean_distance(city_positions[city1], city_positions[city2])

    # Approximate to two decimal places for floating point arithmetic precision issues
    if round(calculated_cost, 2) != round(total_cost, 2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution data
provided_tour = [0, 8, 5, 2, 1, 9, 0]
provided_total_cost = 183.85

# Unit Test Execution
result = verify_solution(provided_tour, provided_total_cost)
print(result)