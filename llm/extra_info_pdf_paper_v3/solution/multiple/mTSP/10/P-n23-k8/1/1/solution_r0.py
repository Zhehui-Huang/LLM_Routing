import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Cities and their coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Using KMeans clustering to assign cities to different robots
city_coords = np.array(list(coordinates.values()))
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords[1:])
labels = kmeans.labels_

# Distances calculation function
def calculate_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

# Tour generator using nearest neighbor heuristic
def generate_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    unvisited_cities = set(cities)
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)
    tour.append(start_city) # Return to depot
    return tour

# Assign cities to robots and generate tours
robots_tours = {}
total_travel_cost = 0

for robot in range(num_robots):
    cities_for_robot = [i+1 for i, label in enumerate(labels) if label == robot] # +1 to skip depot in city list
    tour = generate_tour(0, cities_for_robot)
    robots_tours[robot] = tour

    # Calculate travel cost for each robot
    robot_travel_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_travel_cost}")
    total_travel_cost += robot_travel_cost

print(f"Overall Total Travel Cost: {total_travel_cost}")