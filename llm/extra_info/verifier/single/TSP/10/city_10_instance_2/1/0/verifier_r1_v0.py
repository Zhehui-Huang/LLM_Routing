import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tour(tour, total_cost):
    # Requirement 1: Check if start and end at depot city (Index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if all other cities are visited exactly once
    visited = set(tour[1:-1])  # Exclude the depot city from the list
    if len(visited) != 9 or any(city not in visited for city in range(1, 10)):
        return "FAIL"
    
    # Cities and their coordinates
    cities = {
        0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
        4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
        8: (49, 29), 9: (13, 17)
    }
    
    # Requirement 3: Check total distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour_solution = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
total_travel_cost_solution = 384.7863591860825

# Output verification result
print(verify_tour(tour_solution, total_travel_cost_solution))