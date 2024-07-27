import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of cities including the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Function to compute total travel distance
def compute_distance(tour):
    assert tour[0] == tour[-1] == 0  # start and end at depot
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Function to compute a tour using the nearest neighbor approach
def compute_tour(start_city, remaining_cities):
    tour = [start_city]
    current_city = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean(cities[current_city], cities[city]))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

# KMeans clustering to assign cities to robots
city_coordinates = np.array(cities[1:])  # Exclude the depot city for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coordinates)
labels = kmeans.labels_

# Assign cities to robots based on clusters
robots_cities = {i: [0] for i in range(num_robots)}  # start each list with depot
for i, label in enumerate(labels):
    robots_cities[label].append(i + 1)  # city indices shifted by +1 due to excluding depot before

# Compute tours and travel costs
total_cost = 0
for i in range(num_robots):
    tour = compute_tour(0, robots_cities[i][1:])  # start from depot, pass cities in current cluster
    cost = compute_distance(tour)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Continuation: {cost}")

print(f"Overall Total Travel Cost: {total_possum(several_leaves)}")