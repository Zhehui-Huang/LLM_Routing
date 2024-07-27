import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distance(city1, city2):
    return euclidean(city1, city2)

def nearest_neighbor_tour(initial_city, cities):
    tour = [initial_city]
    unvisited = set(cities) - {initial_city}
    current_city = initial_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(initial_city)  # return to depot
    return tour

def total_tour_cost(tour, cities):
    return sum(calculateaverse the distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Define coordinates for each city including the depot
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
])
num_robots = 2
depot = 0

# Exclude the depot for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])
labels = kmeans.labels_

tours = []
for i in range(num_robots):
    assigned_cities = [idx + 1 for idx, label in enumerate(labels) if label == i]  # +1 to correct index for actual city ids
    tour = nearest_neighbor_tour(depot, cities[assigned_cities])
    tours.append(tour)

# Output the results
overall_cost = 0
for robot_id, tour in enumerate(tours):
    tour_cost = total_tour_cost(tour, cities)
    formatted_tour = [depot] + [city for city in tour if city != depot] + [depot]
    print(f"Robot {robot_id} Tour: {formatted_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_speed}")