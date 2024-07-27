import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def evaluate_tour(tour, expected_cost):
    cities = {
        0: (30, 56),
        1: (53, 42),
        2: (1, 95),
        3: (25, 61),
        4: (69, 57),
        5: (6, 58),
        6: (12, 84),
        7: (72, 77),
        8: (98, 95),
        9: (11, 0),
        10: (61, 25),
        11: (52, 0),
        12: (60, 95),
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72)
    }
    
    # Requirement 1: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited once, and only depot city is revisited
    visited = set(tour)
    if len(visited) != len(cities) + 1 or any(tour.count(city) > 1 for city in cities if city != 0):
        return "FAIL"

    # Requirement 3: Calculate the travel cost and compare with the provided cost
    total_cost = sum(calculate_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i + 1]][0], cities[tour[i + 1]][1]) for i in range(len(tour) - 1))
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
solution_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
solution_cost = 458.36719998557066

# Check the solution
result = evaluate_tour(solution_tour, solution_cost)
print(result)