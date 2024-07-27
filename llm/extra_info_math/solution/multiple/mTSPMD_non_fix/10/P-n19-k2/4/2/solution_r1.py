import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Cities and their coordinates
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots where each robot starts from depot city 0
num_robots = 2

# Generate distance matrix
cities = list(coords.keys())
positions = np.array(list(coords.values()))
dist_matrix = distance_matrix(positions, positions)

# Simple heuristic for Traveling Salesman Problem - Nearest Neighbor for each robot
def tsp_nn(start_city, remaining_cities, dist_matrix):
    tour = [start_city]
    total_cost = 0
    current_city = start_city

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: dist_matrix[current_city][x])
        total_cost += dist_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    
    return tour, total_cost

# Cluster cities into two groups, excluding depot city 
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(positions[1:])
labels = kmeans.labels_

robots_tours = []
robot_total_costs = []

# Assign cities to each robot based on clusters (ignoring depot for now)
for i in range(num_robots):
    robot_cities = [city+1 for city, label in enumerate(labels) if label == i] # +1 to adjust for depot being at 0
    robot_tour, robot_cost = tsp_nn(0, robot_cities, dist_matrix) # Start and end at depot
    robot_tour.append(0) # return to depot
    robot_cost += dist_matrix[robot_tour[-2]][0] # add cost to return to depot
    robots_tours.append(robot_tour)
    robot_total_costs.append(robot_cost)

# Output results
overall_cost = sum(robot_total_costs)
for idx, (tour, cost) in enumerate(zip(robots_tours, robot_total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")