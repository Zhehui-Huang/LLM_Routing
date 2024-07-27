import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def verify_solution(tour, total_travel_cost):
    cities = {
        0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
        4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
        8: (17, 69), 9: (95, 89)
    }
    groups = [
        [5, 6, 7],
        [2, 3],
        [1, 9],
        [4, 8]
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    unique_cities = set(tour[1:-1])  # ignore the first and last city as they are the depot
    for group in groups:
        if len(set(group) & unique_cbeta 0 or len(set(group) & unique_cities) > 1:
            return "FAIL"
    
    # Calculate the travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given tour and total travel cost
tour = [0, 9, 5, 3, 8, 0]
total_travel_cost = 339.8819196935064

# Verification
result = verify_solution(tour, total_travel_cost)
print(result)