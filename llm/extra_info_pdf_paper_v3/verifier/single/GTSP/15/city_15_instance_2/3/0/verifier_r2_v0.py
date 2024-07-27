import numpy as; np

def calculate_euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, city_groups, city_coordinates):
    # Check if the tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(city_groups):
        return False
    
    # Check if tour connects the cities directly
    total_calculated_distance = 0
    for i in range(len(tour) - 1):
        city_pos_a = city_coordinates[tour[i]]
        city_pos_b = city_coordinates[tour[i+1]]
        total_calculated_distance += calculate_euclidean_distance(*city_pos_a, *city_pos_b)

    # The given total cost of the tour
    given_total_cost = 138.15
    
    # Compare the calculated total travel cost with the given total (with some tolerance for floating-point arithmetic)
    if not np.isclose(total_calculated_distance, given_total_cost, atol=0.01):
        return False

    return True

# City Coordinates include depot city as the first element
city_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Given tour
tour = [0, 12, 10, 4, 3, 2, 0]

if verify_tour(tour, city_groups, city_coordinates):
    print("CORRECT")
else:
    print("FAIL")