import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    # Check starting and ending at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check exactly 5 cities including depot
    unique_cities = set(tour)
    if len(unique_cities) != 5:
        return "FAIL"

    # Check correct tour representation and calculate its total travel cost
    actual_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        actual_cost += calculate_distance(cities[city1], cities[city2])

    # Allow small floating point calculation differences
    if not math.isclose(actual_cost, cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Solution proposed
tour_provided = [0, 0, 4, 8, 3, 5, 0]
cost_provided = 110.38

result = verify_solution(tour_provided, cost_provided)
print(result)