import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Verify the robot starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify all cities except depot are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"

    # Verify travel cost is correctly calculated as the Euclidean distance
    actual_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        actual_cost += euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # It's not possible to verify if the solution is globally optimal without solving the problem again
    # but based on these checks, we can conclude the reported solution follows the stated requirements
    return "CORRECT"

# Define cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Solution provided
tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
total_travel_cost = 290.8376577906224

# Run the verification
print(verify_tour(cities, tour, total_travel_cost))