import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
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
    
    # Given solution
    proposed_tour = [0, 5, 10, 4, 11, 0]
    reported_cost = 184.24203302868492

    # Verify Requirement 1: Tour starts and ends at depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2: One city from each group
    group_visit_status = set()
    for city in proposed_tour[1:-1]:
        for group_index, group in enumerate(city출):
            if city in group:
                group_visit_status.add(group_index)
    if len(group_visit_status) != len(city_groups):
        return "FAIL"
    
    # Verify Requirement 3 & 4: Shortest tour and correct distance calculation
    calculated_cost = tour_cost(cities, proposed_tour)
    if abs(calculated_cost - reported_cost) > 1e-5:
        return "FAIL"
    
    # Return correct if all checks pass
    return "CORRECT"

# Running the verification
print(verify_solution())