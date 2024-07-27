import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Group information
    groups = {
        0: [1, 2, 5, 6],
        1: [8, 9, 10, 13],
        2: [3, 4, 7],
        3: [11, 12, 14]
    }
    
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: One city from each group
    visited_groups = set()
    for city in tour:
        for group_id, city_list in groups.items():
            if city in city_list:
                visited_groups.add(group_id)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 5: Correct tour length calculation and one city from each group
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if abs(computed_cost - total_cost) > 0.5:
        return "FAIL"
    
    return "CORRECT"

# Test the verification function with the given solution
solution_tour = [0, 5, 10, 4, 11, 0]
solution_total_cost = 184.24

# Output the result of the solution verification
print(verify_solution(solution_tour, solution_total_cost))