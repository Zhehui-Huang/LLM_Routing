import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution(tour, total_cost):
    # Define the cities' coordinates
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

    # Requirements check
    # Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must include exactly 8 cities
    if len(tour) != 9:  # Includes the return to the starting city
        return "FAIL"
    
    # Requirement 5: Output must be in the correct format
    cities_in_tour = set(tour)
    if len(cities_in_tour) != 9:
        return "FAIL"
    
    # Requirement 4: Each travel segment should use Euclidean distance
    computed_distance = 0
    for i in range(len(tour) - 1):
        computed_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(computed_distance, total_cost, rel_tol=1e-3):
        return "FAIL"

    # Provided that all checks are passed, the solution appears to be correct
    return "CORRECT"

# Given solution
tour = [0, 6, 11, 4, 3, 10, 13, 12, 0]
total_cost = 143.47
result = test_solution(tour, total_cost)
print(result)