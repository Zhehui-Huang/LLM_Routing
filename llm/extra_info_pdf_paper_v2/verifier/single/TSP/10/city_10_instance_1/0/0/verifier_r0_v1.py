import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour, total_cost):
    coordinates = [
        (53, 68),  # Depot city 0
        (75, 11),  # City 1
        (91, 95),  # City 2
        (22, 80),  # City 3
        (18, 63),  # City 4
        (54, 91),  # City 5
        (70, 14),  # City 6
        (97, 44),  # City 7
        (17, 69),  # City 8
        (95, 89)   # City 9
    ]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Allow a small tolerance for floating point arithmetic issues
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Tour and reported total travel cost to test
tour = [0, 5, 2, 9, 7, 1, 6, 4, 8, 3, 0]
reported_cost = 280.84

# Check the solution and print the result
result = check_tour(tour, reported_reported_cost)
print(result)