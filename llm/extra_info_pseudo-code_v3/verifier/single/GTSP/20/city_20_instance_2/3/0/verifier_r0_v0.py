import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour():
    # Cities coordinates
    cities = [
        (3, 26),   # Depot city 0
        (85, 72),  # City 1
        (67, 0),   # City 2
        (50, 99),  # City 3
        (61, 89),  # City 4
        (91, 56),  # City 5
        (2, 65),   # City 6
        (38, 68),  # City 7
        (3, 92),   # City 8
        (59, 8),   # City 9
        (30, 88),  # City 10
        (30, 53),  # City 11
        (11, 14),  # City 12
        (52, 49),  # City 13
        (18, 49),  # City 14
        (64, 41),  # City 15
        (28, 49),  # City 16
        (91, 94),  # City 17
        (51, 58),  # City 18
        (30, 48)   # City 19
    ]

    # Groups of cities
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]

    # Proposed solution
    tour = [0, 11, 16, 18, 19, 6, 0]
    proposed_cost = 162.38

    # Requirement test 1: Tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement test 2: Only one city from each group must be included in the tour
    city_counts = [0] * 20  # There are 20 cities

    for city in tour[1:-1]:  # Exclude the depot city
        city_counts[city] += 1
    
    for group in groups:
        if sum(city_counts[city] for city in group) != 1:
            return "FAIL"

    # Calculate the actual tour cost and compare it
    actual_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour)-1))

    # Consider a small epsilon due to rounding issues in Euclidean distance calculations
    if not math.isclose(proposed_cost, actual_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Running the test
print(test_tour())