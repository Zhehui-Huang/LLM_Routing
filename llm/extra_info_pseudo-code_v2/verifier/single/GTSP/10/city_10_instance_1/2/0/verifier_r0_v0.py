import math

# City coordinates
cities = {
    0: (53, 68),  # Depot
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# City groups
groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

proposed_tour = [0, 9, 5, 3, 8, 0]
proposed_cost = 169.94  # Rounded to two decimal places for the sake of testing

def calculate_euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_starts_and_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

def check_each_group_is_visited_once(tour):
    visited = set(tour[1:-1])  # Excluding the depot at start and end
    for group in groups:
        if not any(city in group for city in visited):
            return False
    return True

def check_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    return round(total_cost, 2) == proposed_cost

def unit_tests():
    if not check_tour_starts_and_ends_at_depot(proposed_tour):
        return "FAIL"
    
    if not check_each_group_is_visited_once(proposed_tour):
        return "FAIL"
    
    if not check_total_travel_cost(proposed_tour):
        return "FAIL"
    
    return "CORRECT"

# Run unit tests
print(unit_tests())