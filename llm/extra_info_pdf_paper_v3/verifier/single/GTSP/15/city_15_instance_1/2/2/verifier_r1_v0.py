import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_positions, city_groups, expected_cost):
    # Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each city group is visited
    visited_groups = set()
    for city_index in tour[1:-1]:
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)

    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check the total travel cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])

    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    # Assuming no explicit verification whether this tour is the shortest possible since that requires solving the problem again or having more context.
    
    return "CORRECT"

# Position of cities where index 0 is depot city
city_positions = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
                  (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
                  (83, 96), (60, 50), (98, 1)]

# Grouping of cities
city_groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Given solution
tour_solution = [0, 5, 10, 4, 11, 0]
total_cost_solution = 184.24203302868492

print(validate_tour(tour_solution, city_positions, city_groups, total_cost_solution))