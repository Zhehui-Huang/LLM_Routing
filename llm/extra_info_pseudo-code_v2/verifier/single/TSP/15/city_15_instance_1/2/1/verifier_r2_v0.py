import math
from itertools import permutations

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(proposed_tour, proposed_cost, cities):
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return False, "Tour must start and end at the depot city 0"
    
    if len(proposed_tour) != len(cities) + 1:
        return False, "Tour should visit each city exactly once plus return to depot"
    
    visited = set(proposed_tour)
    if len(visited) != len(cities):
        return False, "Tour visits some cities more than once or misses some cities"
    
    total_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = proposed_tour[i]
        city2 = proposed_tour[i + 1]
        total_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    
    if not math.isclose(total_cost, proposed_cost, rel_tol=1e-5):
        return False, "Calculated total travel cost does not match the proposed cost"

    # [Requirement 6]: Cannot be verified by execution alone, assumption has to be made that it was used to compute the tour.
    return True, "Success"

def unit_test_solution():
    cities = {
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
    
    proposed_tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
    proposed_cost = 442.570870788815
    
    valid, message = verify_tour_and_cost(proposed_tour, proposed_cost, cities)
    if valid:
        print("CORRECT")
    else:
        print("FAIL:", message)

unit_test_solution()