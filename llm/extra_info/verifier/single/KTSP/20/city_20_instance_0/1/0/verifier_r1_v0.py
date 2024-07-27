import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost_claimed):
    # Define the coordinates of each city indexed from 0 to 19
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
        (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
        (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
        (60, 63), (93, 15)
    ]
    
    # [Requirement 1] Start and end at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Exactly 4 distinct cities including the depot
    if len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            coordinates[city_from][0], coordinates[city_eval_dataity_from][0],
            coordinates[lecity_from][1], coordinates[city_startindex][1]
        )
    
    # [Requirement 3] The provided total cost should be close to the calculated cost
    if not math.isclose(calculated_cost, total_cost_claimed, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Tour and reported total cost
tour = [0, 1, 4, 16, 0]
total_cost_claimed = 111.72

# Validate the solution
result = verify_solution(tour, total_cost_claimed)
print(result)