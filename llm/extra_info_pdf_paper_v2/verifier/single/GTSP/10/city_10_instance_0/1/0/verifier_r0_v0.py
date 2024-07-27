import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_travel_cost, cities, city_groups):
    # Check if the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if there is exactly one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:  # exclude the depot city at both ends for group check
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate total travel cost and compare it to the given cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_travel_cost, computed_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Define city groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Tested tour and cost
test_tour = [0, 6, 7, 5, 0]
test_total_cost = 74.95

# Verify the solution
result = verify_tour(test_tour, test_total_cost, cities, city_groups)
print(result)