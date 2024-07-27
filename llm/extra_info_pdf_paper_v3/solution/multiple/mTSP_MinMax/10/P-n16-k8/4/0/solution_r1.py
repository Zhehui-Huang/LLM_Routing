import numpy as np
from math import sqrt
from sklearn.cluster import KMeans

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City Coordinates
cities = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], 
    [42, 41], [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], 
    [43, 67], [58, 48], [58, 27], [37, 69]
])

# Number of robots
num_robots = 8

# Initialize KMeans clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
labels = kmeans.labels_

# Assign cities to robots based on clusters
robot_routes = {i: [] for i in range(num_robots)}
for i, label in enumerate(labels):
    robot_routes[label].append(i + 1)  # i+1 to adjust indices since city 0 is the depot

# Each robot's tour must start and end at the depot
tours = {}
costs = {}
max_cost = 0
depot = cities[0]

for robot in robot_routes:
    tour = [0]  # start at the depot
    current_city_coords = depot
    route_cost = 0
    
    # Sort cities within cluster to minimize the route distance
    sorted_cities = sorted(robot_routes[robot], key=lambda x: euclidean_distance(depot, cities[x]))
    
    for city in sorted_cities:
        tour.append(city)
        distance = euclidean_distance(current_city_coords, cities[city])
        route_cost += distance
        current_city_coords = cities[city]
    
    # Return to the depot
    distance_back = euclidean_distance(current_city_coords, depot)
    route_cost += distance_back
    tour.append(0)  # end at the depot
    
    tours[robot] = tour
    costs[robot] = round(route_cost, 2)
    if route_cost > max_cost:
        max_cost = route_cost

# Output results
max_cost = round(max_cost, 2)
for robot in tours:
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Maximum Travel Cost: {max_cost}")