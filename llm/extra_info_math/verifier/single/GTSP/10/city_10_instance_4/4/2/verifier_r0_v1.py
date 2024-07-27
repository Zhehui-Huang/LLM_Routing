import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    city_coordinates = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
        4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70), 
        8: (20, 99), 9: (66, 62)
    }
    groups = {
        0: [1, 4], 1: [2, 6], 2: [7], 3: [5], 4: [9], 
        5: [8], 6: [3]
    }
    
    # Check requirement 2
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 1
    visited_cities_from_groups = set([city for city in tour[1:-1] if city in sum(groups.values(), [])])
    if len(visited_cities_from_groups) != len(groups):
        return "FAIL"
    
    # Check requirement 3
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution to test
given_tour = [0, 3, 0]
given_cost = 148.10423709767988

# Verify the solution
print(verify_solution(given_tour, given_cost))