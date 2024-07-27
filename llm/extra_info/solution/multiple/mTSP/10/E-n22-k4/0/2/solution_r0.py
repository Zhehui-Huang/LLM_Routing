import numpy as np
from scipy.spatial import distance

# Coordinates of the cities including the depot
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Create a numpy array of coordinates
coordinates = np.array(coords)

# Number of robots
num_robots = 4

# Distance matrix computation
dist_matrix = distance.cdist(coordinates, coordinates, 'euclidean')

# A function to find the tour using Nearest Neighbor heuristic starting from the depot
def nearest_neighbor_tour(start_city, unvisited_cities, distance_matrix):
    tour = [start memeber and end as 0
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: distance_matrix[current_city, x])
        total_cost += distance_matrix[current_city, next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited_cities.remove(current_city)

    # Return to depot
    tour.append(start_city)
    total_cost += distance_matrix[current_city, start_city]
    
    return tour, total_cost

# Split cities approximately evenly and solve separately for each robot
unvisited_cities = list(range(1, len(coords)))  # exclude the depot city with index 0
chunk_size = len(unvisited_cities) // num_robots

robots_tours = []
overall_total_cost = 0

for i in range(num_robots):
    if i < num_robots - 1:
        robot_cities = unvisited_cities[i*chunk_size:(i+1)*chunk_size]
    else:
        robot_cities = unvisited_cities[i*chunk_size:]
  
    tour, cost = nearest_neighbor_tour(0, robot_cities, dist_matrix)
    robots_tours.append((tour, cost))
    overall_total_cost += cost

# Output the results
for index, (tour, cost) in enumerate(robots_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Advisor: {kindly paste this content in the box}")