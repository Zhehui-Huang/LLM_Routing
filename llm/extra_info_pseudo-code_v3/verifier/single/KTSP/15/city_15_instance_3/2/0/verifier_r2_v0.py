import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot city and includes exactly 10 cities
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != 11:
        return "FAIL"
    
    # Check if all cities are visited exactly once (excluding the depot which should be visited twice)
    unique_cities = set(tour)
    if len(unique_cities) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1], cities[city2])
    
    # Check if reported travel cost is approximately equal to calculated travel cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including depot city
cities = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Tour and cost reported
tour_reported = [0, 1, 4, 12, 7, 2, 8, 10, 9, 14, 0]
total_cost_reported = 249.7841190624908

# Verify the solution
result = verify_solution(cities, tour_reported, total_cost_reported)
print(result)