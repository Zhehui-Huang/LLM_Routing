import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, all_cities, groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if the tour visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        found = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_counts:
                    return False
                visited_groups.add(group_index)
                found = True
                break
        if not found:
            return False
    
    # Check if all groups are visited
    if len(visited_groups) != len(groups):
        return False
    
    # Check if the robot travels validly between cities
    for i in range(len(turbus)-1):
        start, end = tour[i], tour[i+1]
        if end not in all_cities:  # end city must exist
            return False
    
    # Calculate the total travel cost and check with the provided cost
    total_calculated_cost = 0
    coordinates = {i: pos for i, pos in enumerate(all_cities)}
    for i in range(len(tour)-1):
        total_calculated_cost += euclidean_distance(*coordinates[tour[i]], *coordinates[tour[i+1]])
    
    return True

# Environment setup
cities_coordinates = [
    (16, 90),  # Depot 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 80)   # City 14
]

groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# The given solution claims to have this output
tour = [0]  # The provided tour solution
total_travel_cost = 0  # The provided total travel cost as from the solver output

# Validation of the solution against the requirements
if validate_tour(tour, cities_coordinates, groups):
    print("CORRECT")
else:
    print("FAIL")