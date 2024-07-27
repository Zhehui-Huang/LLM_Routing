import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(cities, tour, reported_cost):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities except the depot are visited exactly once
    expected_cities = set(range(len(cities)))  # all cities including depot
    visited_cities = set(tour)
    if visited_cities != expected_cities:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated cost is close to the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Defining cities coordinates
cities = [
    (14, 77),  # city 0
    (34, 20),  # city 1
    (19, 38),  # city 2
    (14, 91),  # city 3
    (68, 98),  # city 4
    (45, 84),  # city 5
    (4, 56),   # city 6
    (54, 82),  # city 7
    (37, 28),  # city 8
    (27, 45),  # city 9
    (90, 85),  # city 10
    (98, 76),  # city 11
    (6, 19),   # city 12
    (26, 29),  # city 13
    (21, 79),  # city 14
    (49, 23),  # city 15
    (78, 76),  # city 16
    (68, 45),  # city 17
    (50, 28),  # city 18
    (69, 9)    # city 19
]

# Provided tour and total cost
provided_tour = [0, 1, 8, 13, 2, 9, 6, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 19, 12, 0]
provided_total_cost = 414.2331847041342

# Verify the tour and cost
result = verify_tour_and_cost(cities, provided_tour, provided_total_cost)
print(result)