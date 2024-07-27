import math
from collections import defaultdict

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost):
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    groups = {
        0: [1, 4],
        1: [2, 6],
        2: [7],
        3: [5],
        4: [9],
        5: [8],
        6: [3]
    }
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = defaultdict(int)
    for city in tour[1:-1]:  # Exclude the depot city at the start and end
        for group_id, cities_in_group in groups.items():
            if city in cities_in_group:
                visited_groups[group_id] += 1
    
    if any(count != 1 for count in visited_groups.values()):
        return "FAIL"
    
    # Calculate and check the total travel cost
    computed_travel_cost = 0
    for i in range(len(tour) - 1):
        computed_travel_dir_cost = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        computed_travel_cost += computed_travel_dir_cost
    
    # Total travel cost should be calculated correctly
    if not math.isclose(computed_travel_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and travel cost
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_travel_cost = 371.19

# Execute the unit test
result = test_solution(tour, total
_travel_cost)
print(result)