import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_travel_cost):
    # Cities' coordinates
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69), 5: (47, 39),
        6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
    }

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(set(tour[1:-1])) != 9 or set(tour[1:-1]) != set(range(1, 10)):
        return "FAIL"

    # [Requirement 3]
    # Already checked by tour ending and starting in city 0 (Requirement 1)

    # [Requirement 4]
    computed_distance = 0
    for i in range(len(tour) - 1):
        computed_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # [Requirement 6]
    if abs(computed_distance - total_travel_cost) > 0.01:
        return "FAIL"

    # [Requirement 5]
    # Implicitly checked by the use of the tour variable representing a list of indices
    
    return "CORRECT"

# Solution data from the user
tour = [0, 9, 4, 8, 3, 2, 5, 1, 6, 7, 0]
total_travel_cost = 284.45

# Verify the solution
result = check_solution(tour, total_travel_cost)
print(result)