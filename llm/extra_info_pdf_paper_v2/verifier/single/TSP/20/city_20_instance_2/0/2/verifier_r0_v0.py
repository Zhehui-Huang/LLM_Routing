import math

# Define the city coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_tour(tour):
    # Requirement 1 and 4
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Requirement 2
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return False

    return True

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    return total_cost

def test_solution(tour, reported_cost):
    # Validate tour requirement 1, 2, and 4
    if not verify_tour(tour):
        return "FAIL"
    
    # Calculate and check the reported total travel cost (requirement 3 and 5)
    calculated_cost = calculate_total_travel_cost(tour)
    if math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "CORRECT"
    else:
        return "FAIL"

# Solution provided
given_tour = [0, 16, 11, 19, 7, 14, 6, 8, 10, 4, 3, 17, 5, 1, 18, 13, 15, 2, 9, 12, 0]
given_total_travel_cost = 487.25038289996235

# Test the solution
result = test_solution(given_tour, given_total_travel_cost)
print(result)