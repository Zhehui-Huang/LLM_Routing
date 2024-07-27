import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_solution(tour, total_cost):
    city_coordinates = {
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
    
    group_definitions = {
        'Group 0': [1, 2, 5, 6],
        'Group 1': [8, 9, 10, 13],
        'Group 2': [3, 4, 7],
        'Group 3': [11, 12, 14]
    }
    
    # Test start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test exact one city from each group
    visited_groups = set()
    for city_idx in tour[1:-1]:  # Exclude the depot city at the start/end
        for group_name, cities in group_definitions.items():
            if city_idx in cities:
                if group_name in visited_groups:
                    return "FAIL"
                visited_groups.add(group_name)
                break
    
    if len(visited_groups) != len(group_definitions):
        return "FAIL"
    
    # Test calculated cost to be correct
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define the provided tour and total travel cost
provided_tour = [0, 5, 10, 4, 11, 0]
provided_total_cost = 184.24203302868492

# Test the solution
test_outcome = test_tour_solution(provided_tour, provided_total_cost)
print(test_outcome)