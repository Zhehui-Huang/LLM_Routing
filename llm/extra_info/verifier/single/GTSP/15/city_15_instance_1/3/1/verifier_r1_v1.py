import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def verify_solution():
    # City coordinates
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
        13: (60, 50),
        14: (98, 1)
    }
    
    # City groups
    city_groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Proposed tour solution
    proposed_tour = [0, 5, 10, 4, 11, 0]
    reported_cost = 184.24203302868492

    # Check if the tour starts and ends at the depot (Requirement 1)
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited (Requirement 2)
    visited_groups = set()
    for city in proposed_tour[1:-1]:
        for index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Verify if the total travel cost is calculated correctly (Requirement 3)
    calculated_cost = tour_cost(cities, proposed_tour)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Return "CORRECT" if all checks pass
    return "CORRECT"

# Running the verification function
print(verify_solution())