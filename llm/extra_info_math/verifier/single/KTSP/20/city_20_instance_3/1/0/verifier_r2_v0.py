import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  
def check_tour():
    cities = {
        0: (30, 56),
        15: (14, 47),
        17: (4, 43),
        5: (6, 58),
        3: (25, 61),
        19: (19, 72),
        6: (12, 84),
        2: (1, 95),
        13: (10, 94),
        12: (60, 95),
        7: (72, 77),
        18: (53, 76),
    }
    
    provided_tour = [0, 15, 17, 5, 3, 19, 6, 2, 13, 12, 7, 18, 0]
    provided_cost = 235.6792673285613
    
    # Check Requirement 1: Starts and ends at depot city 0
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Exactly 13 cities visited
    if len(set(provided_tour)) != 13:
        return "FAIL"
    
    # Check Requirement 3: Travel cost calculation
    total_calculated_cost = 0
    for i in range(len(provided_tour)-1):
        city1, city2 = provided_tour[i], provided_tour[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        total_calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if calculated cost is approximately equal to provided (allowing for minor floating point inaccuracies)
    if not math.isclose(total_calculated_cost, provided_cost, abs_tol=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Run the test
test_result = check_tour()
print(test_result)