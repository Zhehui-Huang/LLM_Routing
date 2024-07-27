import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, total_cost):
    # Defined city coordinates including the depot (city 0)
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # Requirement 1 & 4: Tour must start and end at the depot, and all cities are visited exactly once.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if set(tour) != set(range(20)):
        return "FAIL"

    # Requirement 2: As we use a dictionary 'cities' indexed exactly by city numbers, this requirement is implicitly satisfied.

    # Requirement 3 & 5: Verify the total travel cost.
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):  # Allowing a small tolerance
        return "FAIL"

    return "CORRECT"

# Provided tour and total cost
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 3, 4, 15, 10, 19, 0]
total_cost = 382.53

# Validate the provided solution
result = validate_solution(tour, total_cost)
print(result)