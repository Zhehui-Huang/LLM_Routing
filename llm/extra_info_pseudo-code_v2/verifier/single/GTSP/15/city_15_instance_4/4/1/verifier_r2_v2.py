import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_travel_cost, city_coordinates, groups):
    """ Function to verify the correctness of the provided tour and total travel cost. """
    # Check tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly one city from each group
    visited_groups = {k: False for k in range(len(groups))}
    for city in tour[1:-1]:  # Exclude depot at start and end
        for i, grp in enumerate(groups):
            if city in grp and not visited_groups[i]:
                visited_groups[i] = True
                break
    
    if not all(visited_groups.values()):
        return "FAIL"
    
    # Check total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# City coordinates and groups as given in the problem
city_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Tour and cost provided for verification
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
total_travel_cost = 220.73043826129523

# Execute the verification
result = verify_solution(tour, total_travel_cost, city_coordinates, groups)
print(result)