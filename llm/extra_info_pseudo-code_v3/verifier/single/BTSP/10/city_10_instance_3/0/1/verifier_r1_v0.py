import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    proposed_tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    proposed_total_cost = 555.3286513454195
    proposed_max_distance = 97.04638066409278

    # Check Requirement 1
    if len(set(proposed_tour)) != len(cities) + 1:
        return "FAIL"
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 3 - Implicit by proposed tour.

    # Calculate total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(proposed_tour) - 1):
        dist = calculate_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Check Requirement 4
    if not math.isclose(total_cost, proposed_total_cost, rel_tol=1e-5):
        return "FAIL"

    # Check Requirement 5
    if not math.isclose(max_distance, proposed_max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

print(test_solution())