import math

def euclidean_distance(city1, city2):
    return math.dist(city1, city2)

def test_robot_tour():
    # Define cities coordinates
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }

    # Provided solution
    tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
    reported_total_cost = 132.12

    # Test the solution
    try:
        # [Requirement 1] Starts and ends at depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # [Requirement 2] Exactly 8 cities
        if len(set(tour)) != 8 + 1:  # includes the depot city
            return "FAIL"

        # [Requirement 3 & 5] Check distances and compute total travel cost
        total_calculated_cost = 0
        for i in range(len(tour) - 1):
            city_a = tour[i]
            city_b = tour[i + 1]
            total_calculated_cost += euclidean_distance(cities[city_a], cities[city_b])

        # [Requirement 6] Total travel cost must match reported cost (allowing for some floating-point variation)
        if not math.isclose(total_calculated_cost, reported_total_cost, abs_tol=0.01):
            return "FAIL"

        # Assuming we have checked all requirements, the validation passes assuming no shortest path validation here
        return "CORRECT"

    except Exception as e:
        print(f"An error occurred: {e}")
        return "FAIL"

# Run the test
print(test_robot_tour())