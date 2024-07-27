import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost(solution_tour, solution_cost, city_locations, city_groups):
    # Check if the robot starts and ends at the depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly one city from each defined group of cities
    visited_groups = []
    for city_index in solution_tour:
        for group_index, city_group in enumerate(city_groups):
            if city_index in city_group:
                visited_groups.append(group_index)
    if sorted(list(set(visited_groups))) != sorted(list(range(len(city_groups)))):
        return "FAIL"
    
    # Check if travel cost is computed correctly
    computed_cost = 0
    for i in range(len(solution_tour) - 1):
        computed_cost += calculate_euclidean_distance(city_locations[solution_tour[i]], city_locations[solution_tour[i+1]])
    
    if not math.isclose(solution_cost, computed_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Test data
city_locations = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

solution_tour = [0, 3, 5, 9, 1, 2, 0]
solution_cost = 281.60273931778477

# Execute the test
result = test_tour_and_cost(solution_tour, solution_cost, city_locations, city_groups)
print(result)