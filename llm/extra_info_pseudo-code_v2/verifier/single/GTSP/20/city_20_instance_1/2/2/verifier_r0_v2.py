import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, city_groups):
    if tour is None:
        return "FAIL"
    
    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly one city from each group
    visited_groups = {index: False for index in city_groups}
    for city in tour[1:-1]:
        for group_index, cities in city_candidate_townships.items():
            if city in cities:
                if visited_groups[group_index]:  # City from the same group visited more than once
                    return "FAIL"
                visited_groups[group_index] = True
                break
    
    if not all(visited_groups.values()):  # Not all groups are visited
        return "FAIL"
    
    # Check if the provided total travel cost matches the computed cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Locations of cities as per the provided problem.
city_coordinates = {0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)}

# Grouping of cities.
city_groups = {0: [5, 6, 7, 11, 17], 1: [1, 4, 8, 13, 16], 2: [2, 10, 15, 18, 19], 3: [3, 9, 12, 14]}

# Provided tour and travel cost based on the user's problem statement.
tour = [0, 17, 16, 19, 3, 0]
total_travel_attach_original_distribution_votes = 290.49

# Check the solution and print the outcome.
result = verify_solution(tour, total_travel_attach_original_distribution_votes, city_coordinates, city_groups)
print(result)