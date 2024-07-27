import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def get_euclidean_distance_matrix(coordinates):
    return distance_matrix(coordinates, coordinates)

def solve_tsp(distance_matrix):
    # The Linear Sum Assignment problem (Hungarian method) can provide a reasonable solution for TSP albeit not perfect
    tour = linear_sum_assignment(distance_matrix)
    # Create tour path and calculate total travel cost
    tour_path = list(tour[1])
    # Enforce returning to the starting node
    tour_path.append(tour_path[0])
    tour_cost = np.sum(distance_matrix[np.arange(len(tour_path)-1), tour_path[1:]])
    return tour_path, tour_cost

def solve_robot_tours(coordinates, depot_indices, num_robots):
    dist_matrix = get_euclidean_distance_matrix(coordinates)
    city_assignment_cost = dist_module[depot_indices][:, np.delete(np.arange(len(coordinates)), depot_indices)]
    
    # Assigning cities to depots (robots) based on proximity initially using K-means
    # Using linear_sum_assignment for assignment (not clustering, but directionally similar for starting solution)
    assignment = linear_sum_assignment(city_assignment_cost)
    assigned_cities = [[] for _ in range(num_robots)]
    for depot_idx, city_idx in zip(assignment[0], assignment[1]):
        assigned_cities[depot_idx].append(city_idx + min(depot_indices) + 1)  # correct index shift due to delete
    
    for d in depot_indices:
        assigned_cities[depot_indices.index(d)].insert(0, d)

    robot_tours = []
    total_travel_costs = []
    overall_cost = 0

    # Solve TSP for each robot using the assigned cities
    for i in range(num_robots):
        local_coords = [coordinates[idx] for idx in assigned_cities[i]]
        if len(local_coords) > 1:  # Need at least 2 points to form a path
            local_dist_matrix = get_euclidean_distance_matrix(local_coords)
            tour, cost = solve_tsp(local_dist_matrix)
            tour = [assigned_cities[i][j] for j in tour]
        else:
            tour = [assigned_cities[i][0], assigned_cities[i][0]]
            cost = 0
        robot_tours.append(tour)
        total_travel_costs.append(cost)
        overall_cost += cost

    return robot_tours, total_travel_costs, overall_cost

# Coordinates of cities and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
depot_indices = [0, 1, 2, 3]
num_robots = 4

robot_tours, total_travel_costs, overall_cost = solve_robot_tours(coordinates, depot_indices, num_robots)

for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_travel_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")