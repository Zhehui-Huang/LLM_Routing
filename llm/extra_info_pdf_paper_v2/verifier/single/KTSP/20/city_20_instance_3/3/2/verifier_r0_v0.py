import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    cities = {
        0: (30, 56),
        1: (53, 42),
        2: (1, 95),
        3: (25, 61),
        4: (69, 57),
        5: (6, 58),
        6: (12, 84),
        7: (72, 77),
        8: (98, 95),
        9: (11, 0),
        10: (61, 25),
        11: (52, 0),
        12: (60, 95),
        13: (10, 94),
        14: (96, 73),
        15: (14, 47),
        16: (18, 16),
        17: (4, 43),
        18: (53, 76),
        19: (19, 72)
    }
    
    tour = [0, 3, 15, 5, 19, 6, 13, 2, 12, 7, 14, 4, 1, 0]
    provided_total_cost = 275.9344771267424
    
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly 13 cities including the depot
    if len(tour) != 14:  # Length should be k + 1 because it returns to the depot
        return "FFAIL"

    if len(set(tour)) != 14:
        return "FAIL"

    # Requirement 3 & 4: Check the total tour cost using euclidean distance
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Compare the provided cost with a calculated cost, allowing some tolerance for floating point arithmetic
    if not math.isclose(provided_total_cost, calculated_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the verification function
print(verify_solution())