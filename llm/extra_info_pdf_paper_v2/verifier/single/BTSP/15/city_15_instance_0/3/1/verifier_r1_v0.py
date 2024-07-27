import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(tour, coordinates):
    start_end_condition = tour[0] == 0 and tour[-1] == 0
    unique_visits_condition = len(set(tour)) == len(coordinates) and len(tour) == len(coordinates) + 1

    if not start_end_condition or not unique_visits_condition:
        return "FAIL"

    total_travel_cost = 0
    max_distance_between_cities = 0
    
    for i in range(1, len(tour)):
        distance = euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
        total_travel_cost += distance
        max_distance_between_cities = max(max_distance_between_cities, distance)
    
    # Output from the example solution provided
    example_total_travel_cost = 373.97
    example_max_distance = 63.6

    cost_condition = abs(total_travel_cost - example_total_travel_cost) < 0.01
    max_distance_condition = abs(max_distance_between_cities - example_max_distance) < 0.01

    if cost_condition and max_distance_condition:
        return "CORRECT"
    else:
        return "FAIL"

# Coordinates of each city indexed from 0 to 14
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Provided tour solution
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]

# Check the solution
result = check_solution(tour, coordinates)
print(result)