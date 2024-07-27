import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost):
    # Coordinates for the cities
    cities = [
        (29, 51),  # Depot
        (49, 20),
        (79, 69),
        (17, 20),
        (18, 61),
        (40, 57),
        (57, 30),
        (36, 12),
        (93, 43),
        (17, 36),
        (4, 60),
        (78, 82),
        (83, 96),
        (60, 50),
        (98, 1)
    ]
    
    # Requirement 1: Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if all cities, except depot, are visited exactly once
    seen = set(tour)
    all_cities_set = set(range(1, 15))  # Excluding the depot city which should be at start and end
    if seen.intersection(all_cities_set) != all_cities_set or len(seen) != len(tour):
        return "FAIL"
    
    # Requirement 3: Verify the total cost by calculating the distances
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_total_cost - total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 10, 5, 14, 9, 0]
total_cost = 232.28036302109786

# Test the solution
result = test_solution(tour, total_cost)
print(result)