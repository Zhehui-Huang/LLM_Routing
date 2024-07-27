import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    # City coordinates
    cities = {
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
    
    # Checking Requirement 1: Each city visited once
    unique_cities = set(tour)
    if len(tour) != 11 or len(unique_cities) != len(cities) or not all(city in cities for city in unique_cities):
        return "FAIL"
    
    # Checking Requirement 2: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the travel costs and the maximum segment distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check Requirement 3: Calculated costs should match with given
    if not (math.isclose(calculated_total_cost, total_cost, abs_tol=0.1) and
            math.isclose(calculated_max_distance, max_distance, abs_tol=0.1)):
        return "FAIL"
    
    return "CORRECT"

# Given data from problem description
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32
max_consecutive_distance = 69.43

# Call the verification function and print the result
result = verify_solution(tour, total_travel_cost, max_consecutive_text_check)
print(result)