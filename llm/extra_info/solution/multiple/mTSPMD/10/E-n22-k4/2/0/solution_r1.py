import numpy as np
from scipy.spatial.distance import cdist

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
    
def total_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def nearest_neighbour_tour(start_index, points_count, dist_matrix, visited):
    tour = [start_index]
    current_index = start_index
    while len(tour) < points_count:
        visited[current_index] = True
        distances_to_next = [(dist_matrix[current_index, i], i) for i in range(len(dist_matrix)) if not visited[i]]
        if distances_to_next:
            next_city = min(distances_to_next)[1]
            tour.append(next_city)
            current_index = next_city
    tour.append(start_index)  # return to start
    return tour

def solve_for_robots(coordinates, depots, num_robots):
    num_cities = len(coordinates)
    dist_matrix = cdist(coordinates, coordinates)
    visited = np.zeros(num_cities, dtype=bool)
    
    robot_tours = []
    total_costs = []
    
    for idx in range(num_robots):
        start_city = depots[idx]
        if not visited[start_city]:
            tour = nearest_neighbour_tour(start_city, num_cities, dist_matrix, visited)
            cost = total_tour_cost(tour, dist_matrix)
            robot_tours.append(tour)
            total_costs.append(cost)
    
    overall_cost = sum(total_costs)
    return robot_tours, total_costs, overall_cost

# Coordinates and indices of the depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 207), (141, 206), (147, 293), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]
num_robots = 4

robot_tours, total_travel_costs, overall_cost = solve_for_robots(coordinates, depots, num_robots)

for i in range(num_robots):
    if i < len(robot_tours):
        print(f"Robot {i} Tour: {robot_tours[i]}")
        print(f"Robot {i} Total Travel Cost: {total_travel_costs[i]}")
    else:
        print(f"Robot {i} has no assigned cities.")

print(f"Overall Total Travel Cost: {overall_cost}")