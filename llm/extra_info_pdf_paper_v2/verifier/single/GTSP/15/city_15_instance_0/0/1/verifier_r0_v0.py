import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    # City Coordinates
    cities = {
        0: (9, 93),
        1: (8, 51),
        2: (74, 99),
        3: (78, 50),
        4: (21, 23),
        5: (88, 59),
        6: (79, 77),
        7: (63, 23),
        8: (19, 76),
        9: (21, 38),
        10: (19, 65),
        11: (11, 40),
        12: (3, 21),
        13: (60, 55),
        14: (4, 39)
    }

    # City Groups
    groups = {
        0: [2, 7, 10, 11, 14],
        1: [1, 3, 5, 8, 13],
        2: [4, 6, 9, 12]
    }

    # Check the robot starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check the robot visits exactly one city from each city group
    visited_groups = [0 for _ in range(len(groups))]
    for city in tour[1:-1]:  # Exclude starting and ending depot city
        for group_index, group_cities in groups.items():
            if city in group_cities:
                visited_groups[group_index] += 1

    if any(count != 1 for count in visited_groups):
        return "FAIL"

    # Calculate the total travel cost and check it
    calculated_cost = 0
    for i in range(len(tour)-1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i+1]]
        calculated_cost += euclidean_distance(city_a, city_b)

    # Allowing small floating point error tolerance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided tour and cost
tour = [0, 8, 10, 9, 0]
total_cost = 114.09

# Perform the verification
result = verify_solution(tour, total_cost)
print(result)