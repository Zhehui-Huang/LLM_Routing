import math

# Define the cities' coordinates
cities = [
    (26, 60), # Depot city 0
    (73, 84), # City 1
    (89, 36), # City 2
    (15, 0),  # City 3
    (11, 10), # City 4
    (69, 22), # City 5
    (28, 11), # City 6
    (70, 2),  # City 7
    (47, 50), # City 8
    (60, 29), # City 9
    (29, 26), # City 10
    (85, 68), # City 11
    (60, 1),  # City 12
    (71, 73), # City 13
    (82, 47), # City 14
    (19, 25), # City 15
    (75, 9),  # City 16
    (52, 54), # City 17
    (64, 72), # City 18
    (14, 89)  # City 19
]

# Provided solution
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
provided_cost = 410.04

def calculate_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

def tour_starts_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def visit_all_cities_once(tour):
    return sorted(tour[1:-1]) == list(range(1, 20))

def validate_solution(tour, provided_cost):
    is_correct_start_end = tour_starts_ends_at_depot(tour)
    is_correct_visit = visit_all_cities_once(tour)
    calculated_cost = calculate_cost(tour, cities)
    is_correct_distance = abs(calculated_cost - provided_cost) < 0.1

    if is_correct_start_end and is_correct_visit and is_correct_distance:
        return "CORRECT"
    else:
        return "FAIL"

# Test the solution
print(validate_solution(tour, provided_cost))