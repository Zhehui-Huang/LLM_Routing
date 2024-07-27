import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def validate_tour(cities, tour, groups):
    start_end_condition = (tour[0] == 0 and tour[-1] == 0)
    all_groups_represented = all(any(city in group for city in tour) for group in groups)
    unique_cities = len(set(tour)) == len(tour)

    return start_end_condition and all_groups_represented and unique_cities

def compute_tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        total_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    return total_cost

def verify_solution():
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }
    groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]
    provided_tour = [0, 10, 1, 9, 0]
    provided_cost = 122.21527940040238
    
    if not validate_tour(cities, provided_tour, groups):
        return "FAIL"

    calculated_cost = compute_tour_cost(cities, provided_tour)
    if abs(calculated_cost - provided_cost) > 1e-5:  # Allowing for a slight precision difference
        return "FAIL"

    return "CORRECT"

result = verify_solution()
print(result)