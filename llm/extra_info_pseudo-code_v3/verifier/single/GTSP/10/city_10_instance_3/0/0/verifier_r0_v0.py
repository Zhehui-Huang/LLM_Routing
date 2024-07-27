import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour, city_positions, city_groups, claimed_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city 0

    visited_groups = {}
    total_distance = 0
    
    # Check if tour visits exactly one city per group and calculate total distance
    for i in range(len(tour) - 1):
        city = tour[i]
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"  # More than one city from a group is visited
                visited_groups[group_index] = True
        total_distance += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    # Check if all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check if calculated tour length matches the given total travel cost
    if not math.isclose(total_distance, claimed_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define city positions indexed by city number
city_positions = {
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

# Define groups of cities
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# The solution provided
proposed_tour = [0, 7, 1, 4, 8, 5, 2, 0]
proposed_cost = 324.18

# Validate the solution
result = check_tour(proposed_tour, city_positions, city_groups, proposed_cost)
print(result)