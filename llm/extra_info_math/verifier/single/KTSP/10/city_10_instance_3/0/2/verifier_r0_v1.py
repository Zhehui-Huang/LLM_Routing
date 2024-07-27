import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

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

# Solution provided
tour = [0, 4, 2, 1, 7, 3, 8, 0]
reported_cost = 159.97

# Conditions to check
def check_tour_conditions(tour, reported_cost):
    # Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that exactly 7 cities are visited, including depot
    if len(tour) != 8:  # 7 cities plus the depot visited twice
        return "FAIL"
    
    # Check if the cities are unique (except depot which should appear twice)
    if len(set(tour[:-1])) != 7:
        return "FAIL"

    # Check the total travel cost
    calculated_cost = 0.0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])

    # Compare the float costs with some precision tolerance
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Outputs either "CORRECT" or "FAIL"
result = check_tour_conditions(tour, reported_cost)
print(result)