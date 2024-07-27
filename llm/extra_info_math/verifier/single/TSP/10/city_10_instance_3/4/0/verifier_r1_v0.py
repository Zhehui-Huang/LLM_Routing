import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def test_solution(tour, total_travel_cost):
    # Given data
    positions = {
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
    
    # Check Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Visit all cities exactly once
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"

    # Check Requirement 3: Calculate and verify the total Euclidean distance
    calculated_cost = sum(calculate_euclidean_distance(positions[tour[i]][0], positions[tour[i]][1],
                                                       positions[tour[i+1]][0], positions[tour[i+1]][1])
                           for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Test the solution provided
tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
total_travel_cost = 294.17
result = test_solution(tour, total_travel_to_cost)
print(result)