import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 60),
        14: (98, 1)
    }
    
    groups = [
        [1, 2, 5, 6],  # Group 0
        [8, 9, 10, 13],  # Group 1
        [3, 4, 7],  # Group 2
        [11, 12, 14]  # Group 3
    ]
    
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    group_visit = [set() for _ in groups]
    for city in tour[1:-1]:  # Ignore start/end depot city in the visits
        for i, group in enumerate(groups):
            if city in group:
                group_visit[i].add(city)
    
    if any(len(visits) != 1 for visits in group_visit):
        return "FAIL"
    
    # Calculate the total travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if reported cost is correctly computed
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 11, 13, 5, 0]
total_travel_cost = 148.86963273650017

# Execute the test
test_result = testitivity(tour, total_travel_cost)
print(test_result)