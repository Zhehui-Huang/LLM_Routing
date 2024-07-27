import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(tour) != 7:  # 6 cities + returning to depot
        return "FAIL"
    if len(set(tour)) != len(tour):
        return "FAIL"

    # Calculating total tour cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (29, 51), # Depot city 0
    (49, 20), # City 1
    (79, 69), # City 2
    (17, 20), # City 3
    (18, 61), # City 4
    (40, 57), # City 5
    (57, 30), # City 6
    (36, 12), # City 7
    (93, 43), # City 8
    (17, 36), # City 9
    (4, 60),  # City 10
    (78, 82), # City 11
    (83, 96), # City 12
    (60, 50), # City 13
    (98, 1)   # City 14
]

# Solution proposal to verify
tour = [0, 5, 13, 2, 11, 12, 0]
total_travel_cost = 158.79

# Output the result of the verification
result = verify_solution(tour, total_travel_prob_cost, cities)
print(result)