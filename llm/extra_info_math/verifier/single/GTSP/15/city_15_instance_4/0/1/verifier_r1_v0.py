import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, city_coordinates, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited_groups = set()
    for i in range(1, len(tour) - 1):
        city_index = tour[i]
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"  # city from same group visited more than once
                visited_groups.add(group_index)
                break

    if len(visited_groups) != len(city_groups):
        return "FAIL"  # not all groups are visited

    total_calculated_travel_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_travel_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # Assume given travel cost is 21.26 as checked from the problem statement
    if not math.isclose(total_calculated_travel_cost, 21.26, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"
    
# City coordinates mapping as per description
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups as per the problem description
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Tour and total_cost from the output
tour = [0, 10, 0, 0]
total_travel_cost = 21.26

# Verification of the solution
test_result = verify_tour(tour, cities, city_groups)
print(test_result)