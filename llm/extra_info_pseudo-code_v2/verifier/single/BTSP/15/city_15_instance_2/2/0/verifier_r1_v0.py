import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, coordinates):
    # Check if the tour starts and ends at the depot (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour visits each city exactly once (except for the depot which needs to appear twice)
    unique_cities = set(tour)
    if len(unique_cities) != len(coordinates) or any(city not in unique_cities for city in range(len(coordinates))):
        return "FAIL"

    # Check the calculation of the total distance and max distance between consecutive cities
    total_distance = 0
    max_distance = 0
    for i in range(len(tour)-1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_distance += distance
        max_distance = max(max_distance, distance)

    if not (164.7 < total_distance < 164.71 and 55.3 < max_distance < 55.4):
        return "FAIL"
    
    return "CORRECT"

# Provided coordinates
coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Tour and Solution details
provided_tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
provided_total_cost = 322.5037276986899
provided_max_distance = 64.66065264130884

# Verify the solution
result = verify_solution(provided_tour, coordinates)
print(result)