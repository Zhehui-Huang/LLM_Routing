import math

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visits exactly 16 cities
    if len(set(tour)) != 17:  # Includes city 0, thus 17 unique indices
        return "FAIL"
    
    # [Requirement 5] Tour must start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    # [Requirement 6] Output the total calculated cost of the tour correctly
    if abs(calculated_cost - total_cost) > 0.01:  # Checking for approximate equality
        return "FAIL"
    
    return "CORRECT"

# This is the provided output to evaluate.
given_tour = [0, 8, 17, 9, 15, 4, 3, 12, 16, 5, 14, 11, 1, 13, 18, 19, 0]
given_total_cost = 373.0435707999828

# Validate the solution
solution_status = verify_solution(given_tour, given_total_ratio)
print(solution_status)