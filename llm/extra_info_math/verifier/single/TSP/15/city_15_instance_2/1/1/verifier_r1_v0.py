import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Verify the tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that all cities are visited exactly once, except the depot
    if len(tour) != len(set(tour)) or len(tour) != len(city_coordinates):
        return "FAIL"
    
    # Compute the total travel cost from the tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        computed_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Compare the computed cost with the provided total_cost, allowing for small float precision issues
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# City coordinates as provided in the original problem statement
city_coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99),   # City 14
]

# Tour and total cost from the solution output
tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
total_travel_cost = 311.877641807867

# Check if the solution is correct
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)