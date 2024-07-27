import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_solution(tour, expected_cost):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # Check if all cities except depot are visited exactly once and tour ends at the depot
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:  # Start and end at depot city 0
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1_idx, city2_idx = tour[i], tour[i+1]
        city1, city2 = cities[city1_idx], cities[city2_idx]
        total_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    # Compare the calculated cost with the expected cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided tour solution and expected cost
tour = [0, 14, 5, 7, 4, 16, 10, 11, 13, 12, 17, 18, 15, 19, 2, 8, 3, 1, 9, 6, 0]
expected_cost = 637.267006354176

# Check the solution
result = check_solution(tour, expected_cost)
print(result)