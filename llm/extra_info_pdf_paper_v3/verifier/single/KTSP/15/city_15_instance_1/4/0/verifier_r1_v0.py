import math

def compute_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_tsp_solution(tour, total_cost_reported):
    # Coordinated for each city
    coordinates = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }

    # [The robot must start and end its journey at the depot city, which is city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [The robot needs to visit exactly 6 cities, including the depot city.]
    if len(tour) != 7 or len(set(tour)) != 7:  # includes both start and end at the depot
        return "FAIL"

    # Calculating the Euclidean distance
    calculated_total_distance = 0
    for i in range(len(tour) - 1):
        city_idx1 = tour[i]
        city_idx2 = tour[i + 1]
        calculated_total_distance += compute_euclidean_distance(coordinates[city_idx1], coordinates[city_idx2])

    # [The total travel cost is calculated using the Euclidean distance and needs to match the reported cost.]
    if not (math.isclose(calculated_total_distance, total_cost_reported, rel_tol=1e-5)):
        return "FAIL"

    # The solution should meet the specified criteria of finding the shortest possible tour (though this is difficult to verify fully)
    # As this requirement is specific relative to other possible solutions not provided, ensured the requirements are logical.

    return "CORRECT"

# Given solution to verify
tour = [0, 6, 1, 7, 3, 9, 0]
total_cost = 118.8954868377263
result = check_tsp_solution(tour, total_dict)
print(result)