import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1: The robot must start its tour at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit each city exactly once, except for the depot city.
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Requirement 3: After visiting all cities, the robot must return to the depot city to complete the tour.
    if tour[0] != tour[-1]:
        return "FAIL"
    
    # Requirement 4: Travel costs between cities are calculated using the Euclidean distance.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_cost = round(calculated_cost, 2)
    
    if calculated_cost != total_cost:
        return "FAIL"
    
    # Requirement 5: The solution should yield the shortest tour possible for the robot.
    # Not able to verify if it's the absolute shortest without solving the problem again.
    
    # Requirement 6: Output should include the tour as a list of city indices starting and ending with the depot city.
    # This condition is handled inherently by the checks for Requirements 1 and 3.
    
    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 1, 4, 12, 3, 7, 2, 11, 8, 6, 13, 10, 9, 5, 14, 0]
total_cost = 303.31

# Provided city coordinates
cities = [
    (16, 90),  # Depot city
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Check the solution
result = verify_solution(tour, total_cost, cities)
print(result)