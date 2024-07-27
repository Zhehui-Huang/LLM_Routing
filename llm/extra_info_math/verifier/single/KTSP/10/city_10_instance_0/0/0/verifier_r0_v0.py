import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(cities, tour, expected_cost):
    # Checking Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking Requirement 2: Visit exactly 4 cities including the depot
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"
    
    # Checking Requirement 3: Minimize the total Euclidean distance traveled
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Given solution to test
tour = [0, 5, 6, 9, 0]
total_travel_cost = 65.20172104938949

# Verify the solution
print(verify_tour(cities, tour, total_travel_cost))