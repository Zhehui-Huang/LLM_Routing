import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Cities coordinates
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
    tour = [0, 9, 5, 2, 4, 1, 7, 0]
    reported_cost = 283.99  # As stated
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Check requirements
    correct = True
    errors = []
    
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        correct = False
        errors.append("Requirement 1 failed: Tour does not start and end at the depot city 0.")

    # Requirement 2
    if len(set(tour) - {0}) != 6:
        correct = False
        errors.append("Requirement 2 failed: Tour does not visit exactly 7 unique cities out of 10.")

    # Requirement 3
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-2):
        correct = False
        errors.append(f"Requirement 3 failed: Reported cost and calculated cost are different ({reported_cost} != {calculated_cost}).")

    # Requirement 5
    if not isinstance(tour, list) or not all(isinstance(x, int) for x in tour):
        correct = False
        errors.append("Requirement 5 failed: Output format is incorrect.")
    
    if correct:
        print("CORRECT")
    else:
        print("FAIL")
        for error in errors:
            print(error)

test_solution()