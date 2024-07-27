import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        total_cost += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    return round(total_cost, 2)

def verify_solution():
    # City coordinates with index as city number
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

    # Solution to verify
    tour = [0, 8, 3, 7, 1, 4, 2, 5, 6, 9, 0]
    given_total_cost = 315.56

    # Requirement 4
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Requirement 3
    if len(set(tour)) != len(cities) + 1 or set(tour) != set(cities.keys()).union({0}):
        return "FAIL"

    # Requirement 2
    computed_total_cost = calculate_total_travel_cost(cities, tour)
    if computed_total_cost != given_total =cost or computed_total_cost == 0:
        return "FAIL"

    # Additional validations can be added for Requirement 1 if we run LK algorithm.
    
    # If all checks pass
    return "CORRECT"

# Checking if the provided solution is correct
result = verify_solution()
print(result)