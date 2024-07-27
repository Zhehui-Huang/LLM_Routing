import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost):
    # City coordinates
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if exactly 16 cities, including depot, are visited
    if len(set(tour)) != 16:
        return "FAIL"
    
    # Calculate the tour's actual travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        calculated_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    # [Requirement 3] Check the travel cost calculation
    # Allow a small float difference due to potential precision issues
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-4):
        return "FAIL"
    
    # If all conditions are met
    return "CORRECT"

# Sample solution for verification
tour = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 17, 18, 19, 0]
total_travel_cost = 615.2159197778357

# Check the solution
print(verify_solution(tour, total_travel_cost))