import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, max_consecutive_distance):
    cities = [
        (84, 67),  # Depot city 0
        (74, 40),
        (71, 13),
        (74, 82),
        (97, 28),
        (0, 31),
        (8, 62),
        (74, 56),
        (85, 71),
        (6, 76)
    ]
    
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city must be visited exactly once
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return "FAIL"
    
    # Calculate total cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Check if calculated values match the provided ones
    if not (math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5) and 
            math.isclose(calculated_max_distance, max_consecutive_distance, rel_tol=1e-5)):
        return "FAIL"
    
    return "CORRECT"

# Given solution information
tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
total_travel_cost = 315.5597914831042
max_consecutive_distance = 78.5175139698144

# Verify the solution
result = verify_solution(tour, total_travel_cost, max_consecutive_distance)
print(result)