import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Constants
N_ROBOTS = 8

# Prepare data
data_points = np.array(list(cities.values()))

# KMeans Clustering
kmeans = KMeans(n_clusters=N_ROBOTS, random_state=0).fit(data_points)

# Assign cities to robots
clusters = {i: [] for i in range(N_ROBOTS)}
for i, label in enumerate(kmeans.labels_):
    clusters[label].append(i)

# Calculate each robot's tour using closest neighbour heuristic
def closest_neighbour_tour(cities, start=0):
    tour = [start]
    current = start
    remaining = set(cities.keys()).difference({start})

    while remaining:
        next_city = min(remaining, key=lambda x: euclidean(cities[current], cities[x]))
        tour.append(next_city)
        current = next_city
        remaining.remove(next_city)
        
    tour.append(start)  # return to the depot after visiting all cities
    return tour

# Solving TSP for each robot
def calculate_tour_cost(tour, cities):
    return sum(euclidean(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

robot_tours = {}
max_travel_cost = 0

for robot_id, city_ids in clusters.items():
    assigned_cities = {city_id: cities[city_id] for city_id in city_ids}
    tour = closest_neighbour_tour(assigned_cities, start=0)
    tour_cost = calculate_tour_cost(tour, cities)
    robot_tours[robot_id] = {'tour': tour, 'cost': tour_cost}
    max_travel_cost = max(max_travel_cost, tour_cost)

# Output results
for robot_id in range(N_ROBOTS):
    tour = robot_tours[robot_id]['tour']
    cost = robot_tours[robot_id]['cost']
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")