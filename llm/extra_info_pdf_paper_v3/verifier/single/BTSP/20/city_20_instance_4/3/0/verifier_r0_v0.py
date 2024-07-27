import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_solution():
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
    expected_total_cost = 410.03585920085146
    expected_max_distance = 89.00561780022652

    # Requirement 1 and 2
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if len(set(tour)) != 21:  # considering double visit to depot city
        return "FAIL"

    # Requirement 3 (Partial check, as the full problem requires optimization confirmation)
    calculated_distances = [calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)]
    max_distance = max(calculated_distances)
    if max_distance > expected_max_distance:
        return "FAIL"

    # Requirement 4 and 5
    total_travel_cost = sum(calculated_distances)
    if not math.isclose(total_travel_cost, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-5):
        return "FAIL"

    # Requirement 6 does not need explicit testing as the cities match those provided

    return "CORRECT"

# Execute the test and print the result
print(test_tour_solution())