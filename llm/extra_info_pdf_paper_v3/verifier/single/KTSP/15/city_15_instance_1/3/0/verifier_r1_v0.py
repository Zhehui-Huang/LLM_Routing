import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, total_travel_cost):
    # City coordinates as per the problem statement
    city_coords = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Check Requirement 1: Confirm there are exactly 15 cities
    if len(city_coords) != 15:
        return "FAIL"

    # Check Requirement 3: Robot should visit exactly 6 cities including the depot
    if len(tour) != 7 or len(set(tour)) != 6:
        return "FAIL"
    
    # Check Requirement 2: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Check Requirement 5: Travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a, city_b = tour[i], tour[i + 1]
        a_coords, b_coords = city_coords[city_a], city_coords[city_b]
        calculated_cost += euclidean_distance(a_coords[0], a_coords[1], b_coords[0], b_coords[1])
        
    # Comparing the calculated cost to the provided cost within reasonable precision
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass, return "CORRECT"
    return "CORRECT"

# Test the provided solution
solution_tour = [0, 6, 1, 7, 3, 9, 0]
solution_total_cost = 118.8954868377263

# Print test result
print(test_solution(solution_tour, solution_total_cost))