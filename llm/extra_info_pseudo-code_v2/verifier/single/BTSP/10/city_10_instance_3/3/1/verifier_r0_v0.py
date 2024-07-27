import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_dist):
    # City coordinates given in the problem statement
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Check Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city is visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in cities):
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance
    actual_cost = 0
    actual_max_dist = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_cost += dist
        if dist > actual_max_dist:
            actual_max_dist = dist
    
    # Check Requirement 5: Correct total travel cost
    if not math.isclose(actual_cost, total_cost, abs_tol=0.1):
        return "FAIL"
    
    # Check Requirement 6: Correct max distance between consecutive cities
    if not math.isclose(actual_max_dist, max_dist, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
given_tour = [0, 8, 3, 7, 1, 4, 0]
given_total_cost = 128.73
given_max_distance = 41.11

# Verify the solution
verification_result = verify_solution(given_tour, given_total_cost, given_max_distance)
print(verification_result)