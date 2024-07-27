import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, total_cost):
    # Define the cities coordinates
    cities = {
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
    
    # [Requirement 1] Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly 6 cities, including the depot
    if len(set(tour)) != 6:
        return "FAIL"
    
    # [Requirement 3] Distance calculated using the Euclidean formula
    calculated_distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        calculated_distance += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_distance, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 8, 5, 2, 1, 9, 0]
total_travel_cost = 183.85354044487238  # This should match the manually calculated cost

# Test the solution
result = check_solution(tour, total_travelod_cost)
print(result)