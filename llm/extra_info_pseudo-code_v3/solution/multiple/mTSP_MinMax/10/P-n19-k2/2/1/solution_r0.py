from sklearn.cluster import KMeans
import numpy as np
import itertools

# City coordinates, with the first entry the depot
coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Distance calculation: Euclidean distance
def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of robots
num_robots = 2

# Initialize tours
tours = [[] for _ in range(num_robots)]
tour_costs = [0] * num_robots

# Cluster cities into groups (equal to number of robots)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])  # Excluding depot for clustering
labels = kmeans.labels_

# Assign cities to robots based on clusters and create a start-to-end loop for each
clustered_cities = {i: [] for i in range(num_robots)}
for i, label in enumerate(labels):
    clustered_cities[label].append(i + 1)  # city indices start from 1

# Construct tours for each robot
for robot_id in range(num_robots):
    cities_to_visit = clustered_cities[robot_id]
    current_city = 0  # start at the depot
    robot_tour = [current_city]
    
    while cities_to_visit:
        # Find nearest city to the current city
        nearest_city = min(cities_to_visit, key=lambda x: calculate_distance(coords[current_city], coords[x]))
        cities_to_visit.remove(nearest_city)
        robot_tour.append(nearest_city)
        current_city = nearest_city
    
    # Return to depot
    robot_tour.append(0)
    tours[robot_id] = robot_tour

# Calculate the tour costs and the maximum cost
max_tour_cost = 0

for robot_id in range(num_robots):
    tour = tours[robot_id]
    tour_cost = sum(calculate_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour) - 1))
    tour_costs[robot_id] = tour
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    max_tour_cost = max(max_tour_cost, tour_cost)

print(f"Maximum Travel Cost: {max_tour_cost}")