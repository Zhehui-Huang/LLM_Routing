import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_travel_cost):
    # City coordinates indexed by city number for quick lookup
    city_coordinates = {
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
    
    # Verify Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: Total of exactly 6 cities, including the depot
    if len(tour) != 7 or len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate the tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Verify Requirement 3 & 6: Check the minimized tour cost and provided total travel cost
    if abs(calculated_cost - total_travel_cost) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour_solution = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost_solution = 183.85354044487238

# Verification of the provided solution
result = verify_tour(tour_solution, total_travel_cost_solution)
print(result)