import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost):
    # City coordinates as provided
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
        (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
        (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
        (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    # Checking Requirement 1 and 5: Start at depot (0) and end at depot (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking Requirement 2: Each city except depot must be visited exactly once
    # We can ignore the first and last entry as they are both the depot (0)
    if len(set(tour[1:-1])) != len(cities) - 1:
        return "FAIL"
    
    # Checking Requirement 3: Visiting each city once and then returning to depot is verified by start and end at depot
    
    # Checking Requirement 6: Calculate the provided solution cost and compare with the expected total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1]
        )
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

tour_solution = [0, 14, 16, 11, 7, 10, 3, 4, 1, 19, 17, 5, 6, 8, 2, 9, 15, 13, 18, 12, 0]
total_cost_solution = 692.58

# Checking the solution
result = verify_solution(tour_solution, total_cost_solution)
print(result)