import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Provided solution data
    tour = [10, 5, 3, 0, 0, 0, 0, 0]
    calculated_travel_cost = 90.79160690384901
    
    # Cities coordinates
    cities = {
        0: (14, 77),
        1: (34, 20),
        2: (19, 38),
        3: (14, 91),
        4: (68, 98),
        5: (45, 84),
        6: (4, 56),
        7: (54, 82),
        8: (37, 28),
        9: (27, 45),
        10: (90, 85),
        11: (98, 76),
        12: (6, 19),
        13: (26, 29),
        14: (21, 79),
        15: (49, 23),
        16: (78, 76),
        17: (68, 45),
        18: (50, 28),
        19: (69, 9)
    }
    
    # Requirement 1: Tour must start and finish at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 7 cities including depot
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Requirement 3: Testing the shortest travel cost not applicable since true minimum tour cost is unknown
    # But we should check if calculated cost matches the provided formula and tour
    accumulated_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        accumulated_distance += calculate_euclidean_distance(
            cities[city1][0], cities[city1][1], 
            cities[city2][0], cities[city2][1]
        )
    
    # Round to avoid floating point precision issues, checking nearness instead of exact equality due to potential rounding in the question
    if not math.isclose(accumulated_distance, calculated_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 5: Format of the output is not correct, as it includes redundant zeroes that do not belong
    # to a valid tour of exactly 7 cities.
    return "CORRECT" if len(tour) == 7 else "FAIL"

print(test_solution())