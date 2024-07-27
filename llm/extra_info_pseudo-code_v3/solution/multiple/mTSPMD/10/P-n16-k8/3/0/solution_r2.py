import numpy as np
from scipy.spatial import distance_matrix

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Create distance matrix
locations = list(cities.values())
dist_matrix = distance_matrix(locations, locations)

# Robots information
robots = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7
}

def nearest_neighbor_tour(start_city, dist_matrix):
    num_cities = len(dist_matrix)
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city) # return to depot
    return tour

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

overall_total_cost = 0

# Compute tours for each robot and output results
for robot_id, start_depot in robots.items():
    tour = nearest_neighbor_tour(start_depot, dist_matrix)
    tour_cost = calculate_tour_cost(tour, dist_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_trajectory}")