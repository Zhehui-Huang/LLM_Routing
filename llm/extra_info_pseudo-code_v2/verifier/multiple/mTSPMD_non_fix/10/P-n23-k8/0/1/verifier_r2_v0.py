import math

# Coordinates for the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 
    22: (56, 37)
}

# Solution provided
best_tour = [21, 5, 6, 14, 17, 22, 12, 3, 15, 0, 9, 19, 4, 13, 11, 1, 2, 16, 18, 20, 7, 8, 10]
reported_distance = 461.80779232782646

# Functions to calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Check if all cities are visited exactly once
def test_all_cities_visited_once(tour):
    return sorted(tour) == list(range(len(cities)))

# Check for the correctness of the total travel cost
def test_correct_total_distance(tour, reported_distance):
    calculated_distance = total_tour_distance(tour) 
    return math.isclose(calculated_distance, reported_distance, rel_tol=1e-5)

# Unit tests
def unit_tests():
    if not test_all_cities_visited_once(best_tour):
        return "FAIL: Some cities are not visited or visited more than once."
    if not test_correct_total_distance(best_tour, reported_distance):
        return f"FAIL: Reported distance {reported_distance} does not match calculated distance {total_tour_distance(best_tour)}."
    return "CORRECT"

# Run the tests
print(unit_tests())