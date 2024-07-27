import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at the depot city 0
    
    if len(tour) != len(set(tour)) or len(tour) != len(cities) + 1:
        return "FAIL"  # Tour must visit each city exactly once and end at the depot city
    
    # Check if all cities are visited
    if set(tour) != set(range(len(cities))):
        return "FAIL"  # All cities must be visited
    
    # Calculate the computed travel cost from the tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1_idx = tour[i]
        city2_idx = tour[i + 1]
        computed_cost += calculate_euclidean_distance(cities[city1_idx][0],
                                                      cities[city1_idx][1],
                                                      cities[city2_idx][0],
                                                      cities[city2_idx][1])
    
    # Compare computed travel cost to provided total travel cost
    if not math.isclose(computed_cost, total_cost, abs_tol=0.01):
        return "FAIL"  # The computed cost must be within a small tolerance of the given total cost
    
    return "CORRECT"

# Cities coordinates including depot city 0
cities = [
    (30, 56), # City 0 - depot
    (53, 42), # City 1
    (1, 95),  # City 2
    (25, 61), # City 3
    (69, 57), # City 4
    (6, 58),  # City 5
    (12, 84), # City 6
    (72, 77), # City 7
    (98, 95), # City 8
    (11, 0),  # City 9
    (61, 25), # City 10
    (52, 0),  # City 11
    (60, 95), # City 12
    (10, 94), # City 13
    (96, 73), # City 14
    (14, 47), # City 15
    (18, 16), # City 16
    (4, 43),  # City 17
    (53, 76), # City 18
    (19, 72)  # City 19
]

# Given solution to verify
given_tour = [0, 3, 19, 6, 13, 2, 5, 15, 16, 17, 9, 10, 11, 1, 4, 14, 8, 7, 12, 18, 0]
given_total_cost = 512.80

# Verify the solution
result = verify_tour_and_cost(given_tour, given_total_cost, cities)
print(result)