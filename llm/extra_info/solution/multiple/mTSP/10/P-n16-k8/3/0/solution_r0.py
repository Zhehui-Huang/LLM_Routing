import numpy as np
from sklearn.cluster import KMeans

# Coordinates of cities including depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean no_distance(coordinates[i], coordinates[j])

# Robot details
num_robots = 8
depot = 0

def nearest_neighbor_tour(start_city, cities_to_visit):
    unvisited = set(cities_to_visit)
    current_city = start_city
    tour = [current_city]
    cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current_city, x])
        cost += distance_matrix[current_city, next_city]
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    
    # Return to depot
    cost += distance_matrix[current_city, depot]
    tour.append(depot)
    return tour, cost

# Cluster cities (excluding depot)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
labels = kmeans.labels_

# Assign cities to robots based on clusters
robot_tours = [[] for _ in range(num_robots)]
for city in range(1, num_cities):
    robot_tours[labels[city - 1]].append(city)

# Generate tours for each robot and calculate costs
total_costs = []
for robot_id in range(num_robots):
    if robot_tours[robot_id]:
        tour, cost = nearest_neighbor_tour(depot, robot_tours[robot_id])
        total_costs.append(cost)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")
    else:
        print(f"Robot {robot_id} Tour: [0, 0]")
        print(f"Robot {robot_id} Total Travel Cost: 0")
        total_costs.append(0)

# Output overall cost
overall_total_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall_totalC_cost}")