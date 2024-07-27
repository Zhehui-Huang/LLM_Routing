import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_tour(tour, coordinates):
    # Verify all cities are visited exactly once and the tour returns to the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if sorted(tour) != sorted(list(range(len(coordinates)))):
        return False

    return True

def verify_travel_cost(tour, coordinates, reported_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return math.isclose(total_cost, reported_cost, abs_tol=1e-6)

# Coordinates for each city including the depot
coordinates = [
    (16, 90),  # Depot City 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79),  # City 14
]

# Solution provided
tour_solution = [0, 10, 13, 5, 9, 14, 1, 4, 12, 3, 7, 2, 11, 8, 6, 0]
total_travel_cost_reported = 321.78586424740524

# Main verification
tour_is_correct = verify_tour(tour_solution, coordinates)
cost_is_correct = verify_travel_cost(tour_solution, coordinates, total_travel_cost_reported)

if tour_is_correct and cost_is_correct:
    print("CORRECT")
else:
    print("FAIL")