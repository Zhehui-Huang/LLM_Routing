import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Given problem setup
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    city_groups = [
        [5, 6, 7],
        [2, 3],
        [1, 9],
        [4, 8]
    ]
    
    # Provided solution
    tour = [0, 5, 2, 9, 8, 0]
    reported_cost = 183.99
    
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that exactly one city from each group is visited
    visited_groups = set()
    for index in tour[1:-1]:  # exclude the depot city in the start and end
        for group_id, group in enumerate(city_groups):
            if index in group:
                visited_groups.add(group_id)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the calculated cost is approximately equal to the reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

print(test_solution())