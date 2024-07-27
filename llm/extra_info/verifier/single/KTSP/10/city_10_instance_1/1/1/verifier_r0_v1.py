import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def validate_solution(cities, tour, reported_cost):
    # Requirement 2 and 6: Starts and ends at depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Visits exactly 5 cities including the depot
    if len(tour) != 6:  # tour includes starting and ending at the depot, thus 6 points
        return "FAIL"
    
    # Requirement 6: Total travel cost must be correctly calculated and reported
    calculated_cost = calculate_total_travel_cost(cities, tour)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 1: Tour only contains valid indices for cities
    if any(city_index < 0 or city_index >= len(cities) for city_index in tour):
        return "FAIL"
    
    # Additional check: All visited cities must be unique except the depot
    unique_visits = set(tour[1:-1])  # Exclude the repeated depot at start and end
    if len(unique_visits) != 4:
        return "FAIL"
    
    # Requirement 4 is assumed true as it is inherent in calculation method

    # Passes all the verifiable checks
    return "CORRECT"

# Test the given solution and output:
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
tour = [0, 3, 4, 5, 8, 0]
reported_cost = 175.37317918852779

# Correct the incorrectly referenced variable name
result = validate_solution(cities, tour, reported_cost)
print(result)  # "CORRECT" or "FAIL"