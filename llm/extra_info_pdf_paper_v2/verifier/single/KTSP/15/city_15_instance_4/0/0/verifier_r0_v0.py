import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost):
    cities = [
        (35, 40),  # Depot city 0
        (39, 41),
        (81, 30),
        (5, 50),
        (72, 90),
        (54, 46),
        (8, 70),
        (97, 62),
        (14, 41),
        (70, 44),
        (27, 47),
        (41, 74),
        (53, 80),
        (21, 21),
        (12, 39)
    ]

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 12 cities, including the depot
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Requirement 3: The tour provided doesn't directly validate the optimality,
    # we only check path calculation and city count
    computed_cost = 0
    for i in range(1, len(tour)):
        computed_cost += calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    
    # Requirement 4: Check calculated cost matches given total travel cost with a tolerance for float precision errors
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given tour and total travel cost from the problem
tour = [0, 0, 0, 0, 10, 14, 6, 11, 12, 4, 7, 9, 0]
total_travel_cost = 232.23044386972205

# Call the test function
output = test_solution(tour, total_travel_cost)
print(output)