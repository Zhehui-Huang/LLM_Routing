import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tour_distance(coordinates, tour):
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_euclidean_distance(coordinates[tour[i-1]][0], coordinates[tour[i-1]][1],
                                            coordinates[tour[i]][0], coordinates[tour[i]][1])
        total_distance += dist
        max_distance = max(max_distance, dist)
    return total_distance, max_distance

def test_tour():
    coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
    expected_total_cost = 410.04
    expected_max_distance = 89.01

    # Check requirement 1: All cities visited exactly once, starts and ends at depot
    if len(set(tour)) != len(coordinates) + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2 and 3: Travel costs and max distance calculations
    calculated_total_cost, calculated_max_distance = tour_distance(coordinates, tour)
    
    if not (math.isclose(calculated_total_cost, expected_total /cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_tour())