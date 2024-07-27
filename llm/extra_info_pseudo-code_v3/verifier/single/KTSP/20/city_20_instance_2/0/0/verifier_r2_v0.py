import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }
    
    # Check Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visits exactly 10 cities
    if len(tour) != 11:  # includes repeated depot city start and end
        return "FAIL"
    
    # Check Requirement 4: Proper tour representation
    if not all(isinstance(city, int) and city in cities for city in tour):
        return "FAIL"
    
    # Calculate and check Requirement 3: Validate the total cost calculation
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_calculated investment_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 5 implicitly satisfied by format of output and input check

    return "CORRECT"

# Testing with the provided solution
tour_provided = [0, 14, 8, 10, 7, 18, 13, 11, 16, 19, 0]
total_cost_provided = 211.18923578591256

result = test_solution(tour_provided, total_cost_provided)
print(result)