import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour_and_cost(tour, expected_cost, city_coordinates, city_groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_idx, group in enumerate(city_lists):
            if city in group:
                visited_groups.add(group_idx)
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the total cost and compare with the reported cost
    total_calculated_cost = 0
    for i in range(len(tour)-1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_calculated_cost += calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])
    
    if not math.isclose(total_calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City Coordinates
city_coordinates = [
    (9, 93),  # depot
    (8, 51), 
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Groups of cities
city_lists = [
    [2, 7, 10, 11, 14],  # group 0
    [1, 3, 5, 8, 13],    # group 1
    [4, 6, 9, 12]        # group 2
]

# Solution provided
tour_solution = [0, 8, 10, 9, 0]
total_travel_cost_solution = 114.09092744482805

# Verify
result = verify_tour_and_cost(tour_solution, total_travel_cost_solution, city_coordinates, city_lists)
print(result)