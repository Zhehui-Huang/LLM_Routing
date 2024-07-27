import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_tour(tour, groups, cities, expected_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city_index in tour:
        for group_index, group in enumerate(groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Check the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Provided solution
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_travel_cost = 324.18

# Verify the provided solution
result = verify_tour(tour, groups, cities, total_travel_cost)
print(result)