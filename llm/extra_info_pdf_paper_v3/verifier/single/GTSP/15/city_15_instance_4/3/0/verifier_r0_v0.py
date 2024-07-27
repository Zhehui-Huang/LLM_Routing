import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour():
    # City coordinates grouped by city index
    coordinates = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Groups as provided, with sets for checking
    groups = [
        {3, 8}, {4, 13}, {1, 2}, {6, 14}, {5, 9}, {7, 12}, {10, 11}
    ]
    
    # Proposed tour and expected cost
    tour = [0, 1, 5, 7, 4, 6, 3, 10, 0]
    reported_cost = 223.46

    # Check Requirement 1: One city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude starting and ending depot
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups.append(idx)
    
    if len(set(visited_groups)) != len(groups):
        return "FAIL"
    
    # Check Requirement 2: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 3: Correct calculation of travel cost
    calculated_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    
    # Allowing for minor floating-point errors in manual cost calculations
    if not math.isclose(calculated_cost, reported_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test
result = test_tour()
print(result)