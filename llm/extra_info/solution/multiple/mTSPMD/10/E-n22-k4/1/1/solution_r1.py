import numpy as np

# Given coordinates of cities (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i, j] = euclidean_distance(coords[i], coords[j])
            else:
                dist_matrix[i, j] = float('inf')  # No loops
    return dist_matrix

def nearest_neighbor_tour(start, unvisited, distances):
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # Return to the depot
    return tour

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Compute distance matrix
dist_matrix = calculate_distances(coordinates)

# Split cities among robots
team_assignments = {
    0: [0] + list(range(4, 10)),
    1: [1] + list(range(10, 15)),
    2: [2] + list(range(15, 19)),
    3: [3] + list(range(19, 22))
}

overall_total_cost = 0

# Find tours for each robot
for robot_id in range(4):
    depot = team_assignments[robot_id][0]
    cities_to_visit = set(team_assignments[robot_id][1:])
    tour = nearest_neighbor_tour(depot, cities_to_visit, dist_matrix)
    tour_cost = calculate_tour_cost(tour, dist_matrix)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")