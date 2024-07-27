import math

# Given city coordinates
cities = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Solution provided
tour = [0, 4, 1, 8, 13, 17, 5, 19, 2, 6, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 351.47
max_dist_between_consecutive_cities = 32.39

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, total_travel_cost, max_dist_between_consecutive_cities):
    if tour[0] != tour[-1] or tour[0] != 0:
        return "FAIL"
    if len(tour) != len(set(tour)):
        return "FAIL"
    calculated_total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        distance = calculate_distance(city1, city2)
        calculated_total_distance += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    if round(calculated_total_distance, 2) != total_travel_cost:
        return "FAIL"
    if round(calculated_max_distance, 2) != max_dist_between_consecutive_cities:
        return "FAIL"
    return "CORRECT"

# Run validation and print result
result = validate_tour(tour, total_travel_cost, max_dist_between_consecutive_cities)
print(result)