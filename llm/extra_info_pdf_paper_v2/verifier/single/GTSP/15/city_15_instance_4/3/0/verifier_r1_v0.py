import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_solution(tour, cities, groups):
    # Check start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check one city from each group is visited
    visited_groups = set()
    for city_index in tour:
        for group_index, group_cities in enumerate(groups):
            if city_index in group_cities:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate and verify the total travel cost
    expected_cost = 156.832807132982
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define city and group details from the scenario
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}
groups = [
    [3, 8],    # Group 0
    [4, 13],   # Group 1
    [1, 2],    # Group 2
    [6, 14],   # Group 3
    [5, 9],    # Group 4
    [7, 12],   # Group 5
    [10, 11]   # Group 6
]

# Given solution to verify
tour = [0, 13, 14, 8, 10, 12, 5, 1, 0]

# Verify the tour based on requirements
result = verify_tour_solution(tour, cities, groups)
print(result)