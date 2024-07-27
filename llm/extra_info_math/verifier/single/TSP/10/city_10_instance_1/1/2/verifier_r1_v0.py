import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1 or any(city not in visited_cities for city in range(1, len(cities))):
        return "FAIL"
    
    # Check if each city is arrived at and departed from exactly once
    for i in range(1, len(cities)):
        if tour.count(i) != 1:
            return "FAIL"
    
    # Check for subtours (not required explicitly as all cities are visited exactly once)
    
    # Compute the total cost of the tour and compare with the given objective value (solution cost must be minimum or almost equal)
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        
    return "CORRECT" if abs(computed_cost - 278.93) < 1e-2 else "FAIL"
    
# City coordinates
cities = [
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

# Given tour from the result
tour = [0, 6, 1, 7, 9, 2, 5, 3, 8, 4, 0]

# Perform verification
verification_result = verify_solution(tour, cities)
print(verification_result)