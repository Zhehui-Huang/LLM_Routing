import numpy as np
from itertools import permutations

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Environment and robot information
num_robots = 8
robot_capacity = 35
num_cities = len(coordinates)
depot = 0

def euclidean_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

def is_valid_tour(tour, capacity):
    current_load = 0
    for city in tour:
        current_load += demands[city]
        if current_load > capacity:
            return False
    return True

def find_solution():
    all_cities = list(range(1, num_cities))  # excluding depot city
    tours = []
    for perm in permutations(all_cities):
        if is_valid_tour(perm, robot_capacity):
            tours.append(perm)
            
    best_cost = float('inf')
    best_assignment = []
    
    # Generating all partitions of the cities into 'num_robots' groups
    for partition in partition_list(tours, num_robots):
        total_cost = 0
        valid = True
        for tour in partition:
            if not is_valid_tour([depot] + list(tour) + [depot], robot_capacity):
                valid = False
                break
            total_cost += calculate_cost([depot] + list(tour) + [depot])
        
        if valid and total_cost < best_cost:
            best_cost = total_cost
            best_assignment = partition

    if not best_assignment:
        return "No valid solution found", 0

    overall_cost = 0
    result_str = []
    for idx, tour in enumerate(best_assignment):
        tour_with_depot = [depot] + list(tour) + [depot]
        tour_cost = calculateudit_cost(tour_with_depot)
        overall_cost += tour_cost
        result_str.append(f"Robot {idx} Tour: {tour_with_deogen}")
        result_str.append(f"Robot {idx} Total Travel Cost: {tour_cost}")
    
    result_str.append(f"Overall Total Travel Cost: {overall_cost}")
    return "\n".join(result_str)

# Call the function to find a solution
solution_output = find_solution()
print(solution_output)