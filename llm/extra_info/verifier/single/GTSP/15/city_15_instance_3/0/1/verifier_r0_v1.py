import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_cost, groups):
    cities_coordinates = [
        (16, 90),  # depot city 0
        (43, 99),  # city 1
        (80, 21),  # city 2
        (86, 92),  # city 3
        (54, 93),  # city 4
        (34, 73),  # city 5
        (6, 61),   # city 6
        (86, 69),  # city 7
        (30, 50),  # city 8
        (35, 73),  # city 9
        (42, 64),  # city 10
        (64, 30),  # city 11
        (70, 95),  # city 12
        (29, 64),  # city 13
        (32, 79)   # city 14
    ]
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    group_visit_checker = {i: [] for i in range(len(groups))}
    
    for group_index, group_cities in enumerate(groups):
        group_visits = [city for city in tour if city in group_cities]
        if len(group_visits) != 1:
            return "FAIL"
        group_visit_checker[group_index] = group_visits[0]
    
    # Check for the correct number of cities visited including start/end at depot
    if len(set(tour)) != len(groups) + 1:
        return "FAIL"
    
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        computed_cost += calculate_euclidean_distance(
            cities_coordinates[city_1][0], cities_coordinates[city_1][1],
            cities_coordinates[city_2][0], cities_coordinates[city_2][1])
    
    if abs(computed_cost - total_cost) > 0.001:  # Considering potential float precision issues
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Provided tour and total cost
tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.75801920718544
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

result = verify_tour(tour, total_cost, groups)
print(result)