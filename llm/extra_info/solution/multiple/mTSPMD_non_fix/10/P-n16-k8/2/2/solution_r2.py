import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def calculate_distance(point1, point2):
    return euclidean(point1, point2)

def nearest_neighbor_tour(start, cities, all_coords):
    tour = [start]
    current = start
    unvisited = set(cities)
    unvisited.remove(start)

    while unvisited:
        next_city = min(unvisited, key=lambda x: calculate_distance(all_coords[current], all_coords[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    return tour

# Cities' coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
])

# Number of robots
num_robots = 8
robots = range(num_robots)
starting_depot = 0

# Cluster cities for the initial groups for robots (considering all cities including the depot)
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates)
clusters = kmeans.labels_

tours = []
tour_costs = []
overall_cost = 0

for i in robots:
    cities_in_cluster = [index for index, label in enumerate(clusters) if label == i]
    # Ensure depot is in the tour, bring it to the start if it's not
    if starting_depot in cities_in_cluster:
        cities_in_cluster.remove(starting_depot)
    cities_in_cluster.insert(0, starting_depot)

    # Find a tour starting and ending at the depot city for each robot
    tour = nearest_neighbor_tour(starting_depot, cities_in_cluster, coordinates)
    # Add the starting depot to the start and end for complete closure of the loop
    tours.append(tour)

    # Calculate tour costs
    tour_cost = sum(calculate_distance(coordinates[tour[j]], coordinates[tour[j + 1]]) for j in range(len(tour) - 1))
    tour_costs.append(tour_cost)
    overall_cost += tour_cost

# Printing results
for robot_idx, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {robot_idx} Tour: {tour}")
    print(f"Robot {robot_idx} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", overall_cost)