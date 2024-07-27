import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def validate_solution(tour, total_travel_cost):
    # City coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
        6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
        11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }

    # Check if the provided tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 8 cities are visited
    if len(set(tour)) != 8:
        return "FAIL"

    # Calculate the tour length
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += euclidean_distance(cities[city1], cities[city2])

    # Check if the calculated cost matches the total travel cost provided
    if not math.isclose(calculated to tal_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_travel_cost = 132.1185774560832

# Validate the provided solution
result = validate_solution(tour, total_travel_cost)
print(result)