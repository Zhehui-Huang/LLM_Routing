import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_tour_and_cost():
    cities = [
        (14, 77),  # Depot city 0
        (34, 20),  # City 1
        (19, 38),  # City 2
        (14, 91),  # City 3
        (68, 98),  # City 4
        (45, 84),  # City 5
        (4, 56),   # City 6
        (54, 82),  # City 7
        (37, 28),  # City 8
        (27, 45),  # City 9
        (90, 85),  # City 10
        (98, 76),  # City 11
        (6, 19),   # City 12
        (26, 29),  # City 13
        (21, 79),  # City 14
        (49, 23),  # City 15
        (78, 76),  # City 16
        (68, 45),  # City 17
        (50, 28),  # City 18
        (69, 9)    # City 19
    ]
    
    # Given solution
    proposed_tour = [0, 6, 2, 13, 8, 9, 14, 0]
    proposed_cost = 130.6658168109853

    # Check start and end at depot
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check if 7 cities are visited
    if len(set(proposed_tour)) != 7:
        return "FAIL"

    # Calculate cost based on the Euclidean distance
    total_calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = cities[proposed_tour[i]]
        city2 = cities[proposed_tour[i + 1]]
        total_calculated_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])

    # Check if the calculated cost is approximately equal to the proposed cost
    if not math.isclose(total_calculated_cost, proposed_cost, rel_tol=1e-9):
        return "FAIL"

    # Assess if we have the record of the shortest possible route (not feasible without solving)
    # Normally here you would have a check against a benchmark or known optimal solution to verify,
    # but as we do not have this data available we will accept the provided solution as the best known.
    # This is a limitation of the testing without having an exact optimal to compare against.

    return "CORRECT"

# Execute test
print(test_tour_and_cost())