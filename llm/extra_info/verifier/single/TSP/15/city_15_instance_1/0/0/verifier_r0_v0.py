import math

# Cities coordinates including the depot city
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between points a and b """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def validate_solution(tour, total_travel_cost_actual):
    # Check if tour starts and ends at the depot city 0
    starts_and_ends_at_depot = tour[0] == 0 and tour[-1] == 0
    
    # Check if all cities except depot are visited exactly once
    visited_cities = set(tour)
    all_cities_visited_once = set(range(1, 15)) == visited_cities - {0}
    
    total_travel_cost_calculated = 0

    # Calculate the total travel cost from the tour
    for i in range(len(tour) - 1):
        total_travel_cost_calculated += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Calculate the correct actual travel cost within a tolerance for possible float arithmetic issues
    travel_cost_correct = math.isclose(total_travel_cost_calculated, total_travel_cost_actual, rel_tol=1e-9)

    if starts_and_ends_at_depot and all_cities_visited_once and travel_cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Provided solution
tour = [0, 0]
total_travel_cost_actual = 0.0

# Validate the solution
result = validate_solution(tour, total_travel_cost_actual)
print(result)