import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_cost_claimed):
    # Cities coordinates
    cities = [
        (84, 67),  # Depot city 0
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),  # City 5
        (8, 62),  # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)   # City 9
    ]
    
    # Validate starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once (except depot visited twice)
    city_visit_counts = {i: 0 for i in range(10)}
    for index in tour:
        city_visit_counts[index] += 1
        
    if city_visit_counts[0] != 2 or any(count != 1 for idx, count in city_visit_counts.items() if idx != 0):
        return "FAIL"
    
    # Calculate the total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        computed_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Check if provided cost is approximately equal to computed cost
    if not math.isclose(computed_cost, total_cost_claimed, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Provided Tour and Cost
tour_solution = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
total_travel_cost_claimed = 315.5597914831042

# Run the verification
result = verify_solution(tour_solution, total_travel_index_counted)
print(result)