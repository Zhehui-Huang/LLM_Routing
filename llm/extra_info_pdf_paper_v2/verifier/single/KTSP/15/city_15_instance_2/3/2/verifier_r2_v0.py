import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    # Cities coordinates
    cities_coordinates = {
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
        14: (6, 99),
    }

    # Solution provided
    tour = [0, 2, 12, 4, 3, 1, 11, 6, 0]
    reported_cost = 154.59878090164597

    # [Requirement 1] Starts and ends at city 0
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at depot city, city 0."

    # [Requirement 2] Exactly 8 cities including the depot city
    assert len(set(tour)) == 8, "Tour does not visit exactly 8 cities, including the depot city."

    # [Requirement 3 & 4] Calculate total travel cost and check if it matches
    calculated_total_cost = sum(calculate_euclidean_distance(cities_coordinates[tour[i]][0], 
                                                             cities_coordinates[tour[i]][1], 
                                                             cities_coordinates[tour[i+1]][0], 
                                                             cities_coordinates[tour[i+1]][1])
                                 for i in range(len(tour) - 1))
    
    # Check for approximate equality, considering possible floating point arithmetic issues
    assert math.isclose(calculated_total_cost, reported_cost, rel_tol=1e-9), "Reported cost does not match calculated cost."

    print("CORRECT")

try:
    test_solution()
except AssertionError as e:
    print("FAIL:", str(e))