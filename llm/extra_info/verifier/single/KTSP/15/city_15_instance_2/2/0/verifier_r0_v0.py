import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    # Check if the route starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the route includes exactly 8 cities
    if len(tour) != 9:  # including the depot twice
        return "FAIL"
    
    # Ensure all cities in the tour are unique except the start and end
    if len(set(tour)) != 8:
        return "FAIL"

    # Calculate the travel cost and verify against the given total cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = cities[tour[i - 1]]
        x2, y2 = cities[tour[i]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)

    # Check if the calculated travel cost matches the provided total cost (tolerance for floating point precision issues)
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
result = verify_solution([0, 2, 13, 3, 4, 12, 11, 6, 0], 132.1186)
print(result)