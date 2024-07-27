import math
from sklearn.cluster import KMeans

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(start, cities):
    tour = [start]
    current_city = start
    local_cities = cities[:]
    
    while local_cities:
        next_city = min(local_cities, key=lambda city: calculate_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        current_city = next_city
        local_cities.remove(next_city)
    
    tour.append(start)  # return to depot
    return tour

# Number of robots
num_robots = 8

# Exclude the depot for clustering
city_indices = list(range(1, len(coordinates)))

# KMeans Clustering to assign cities to the closest depot
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
clusters = {i: [] for i in range(num_robots)}
for i, label in enumerate(kmeans.labels_):
    clusters[label].append(city_indices[i])

# Construct tours for each robot and calculate distances
total_cost = 0
for robot_id, cities in clusters.items():
    if cities:
        tour = nearest_neighbor_tour(0, cities)
        tour_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    else:
        print(f"Robot {robot_id} Tour: [0, 0]")
        print(f"Robot {robot_id} Total Travel Cost: 0")

print(f"Overall Total Travel Cost: {total_cost}")