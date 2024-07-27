import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost_claimed):
    # City coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # City groups
    groups = [
        [1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]
    ]
    
    # Check requirement 1: Starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: Visit one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot (start and end)
        for index, group in enumerate(groups):
            if city in group:
                visited_groups.add(index)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check requirement 5: Tour starting and ending at city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check requirement 3 & 6: Correct calculation of the tour's total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Allow small floating-point discrepancies
    if not math.isclose(calculated_cost, total_cost_claimed, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Given example solution
provided_tour = [0, 5, 10, 4, 11, 0]
provided_cost = 184.24

# Output the validation result
print(verify_tour(provided_tour, provided_cost))