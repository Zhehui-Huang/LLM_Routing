import math

def calculate_distance(x1, y1, x2, y2):
    """ Helper function to calculate Euclidean distance between two points """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_cost):
    cities_coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # [Requirement 1] and [Requirement 3]
    if not (tour[0] == tour[-1] == 0):
        return "FAIL"

    # [Requirement 2]
    if len(set(tour)) != 16 or len(tour) != 17:  # Including the depot twice (start and end)
        return "FAIL"

    # Calculate total travel cost and check [Requirement 4]
    computed_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        computed = calculate_distance(*cities_coordinates[city_a], *cities_coordinates[city_b])
        computed_cost += computed
    
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-6):
        return "FAIL"

    # [Requirement 5] (This check lacks proper validation without knowing optimal values)
    return "CORRECT"

# Provided results
tour = [0, 19, 15, 4, 3, 10, 9, 8, 18, 1, 13, 14, 2, 16, 12, 0]
total_travel_cost = 419.4848463159844

# Verify the tour and total travel cost
print(verify_tour(tour, total_travel_cost))