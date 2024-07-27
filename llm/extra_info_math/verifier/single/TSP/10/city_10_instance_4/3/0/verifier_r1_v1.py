import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities, reported_cost):
    # Check Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit all cities exactly once
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != len(cities) or any(city not in unique_cities_visited for city in range(len(cities))):
        return "FAIL"

    # Check Requirement 3: Validate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_cost = round(calculated_cost, 2)  # Assuming similar rounding as reported

    if abs(calculated_cost - reported_cost) > 0.1:  # Allow a small margin for floating point arithmetic variations
        return "FAIL"

    return "CORRECT"

# Test configuration
tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
reported_cost = 320.79
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Perform the test
result = verify_solution(tour, cities, reported_cost)
print(result)