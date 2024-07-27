import math

def calc_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_solution(cities, tour, reported_cost):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (excluding the depot city, which must be visited twice)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calc_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the calculated travel cost matches the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates provided
cities = [
    (54, 87),  # City 0
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
    (6, 99)    # City 14
]

# Tour reported from optimization result
reported_tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
reported_cost = 311.877641807867

# Verify solution
result = verify_tour_solution(cities, reported_tour, reported_cost)
print(result)