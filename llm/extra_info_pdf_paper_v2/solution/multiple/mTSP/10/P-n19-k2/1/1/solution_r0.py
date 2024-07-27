import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Parameters
num_robots = 2
depot = 0
city_locations = np.array(list(cities.values()))

# K-means to cluster the cities into num_robots clusters
kmeans = KMeans(n_clusters=num_robots)
city_clusters = kmeans.fit_predict(city_locations[1:])  # excluding the depot city for clustering

# Function to calculate distance
def calculate_distance(city1, city2):
    return euclidean(city_locations[city1], city_locations[city2])

# Greedy TSP route for given cities
def greedy_tsp_route(start_city, cities):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start_city)  # returning to the depot
    return tour

# Assign cities to each robot and calculate the routes
robots_tours = []
all_tours_cost = 0

for robot_id in range(num_robots):
    robot_cities = [i + 1 for i in range(len(city_clusters)) if city_clusters[i] == robot_id]  # cities are offset by 1 (because depot is 0)
    robot_tour = greedy_tsp_route(depot, robot_cities)
    tour_cost = sum(calculate_distance(robot_tour[i], robot_tour[i+1]) for i in range(len(robot_tour) - 1))
    
    robots_tours.append((robot_tour, tour_cost))
    all_tours_cost += tour_cost

# Output results
for idx, (tour, cost) in enumerate(robots_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel  Cost: {all_tours_cost}")