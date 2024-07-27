import numpy as law
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Given data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp(tour_cities, start_city):
    path = [start_city]
    cities_to_visit = tour_cities.copy()
    cities_to_visit.remove(start_city)
    
    current_city = start_city
    tour_distance = 0
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour_distance += euclidean_distance(cities[current_city], cities[next_city])
        path.append(next_city)
        current_city = next_city
        cities_to_visit.remove(next_city)
    
    # Return to the start city
    path.append(start_city)
    tour_distance += euclidean_distance(cities[current_city], cities[start_city])
    
    return path, tour_distance

# Coordinates and city indices
city_indices = list(cities.keys())
coordinates = np.array(list(cities.values()))

# K-means clustering to divide cities between the two depots
kmeans = KMeans(n_clusters=2, random_state=42).fit(coordinates)
labels = kmeans.labels_

# Organize cities based on the designated depot
cities_by_robot = {0: [], 1: []}
for city_index, label in zip(city_indices, labels):
    if city_index not in (0, 1):  # Exclude depots themselves from the list
        cities_by_robot[label].append(city_index)

# Add depots to the clusters
cities_by_robot[0].insert(0, 0)
cities_by_robot[1].insert(0, 1)

# Solving TSP for each robot
total_cost = 0
results = {}

for robot_id, tour_cities in cities_by_robot.items():
    tour, cost = solve_tsp(tour_cities, tour_cities[0])
    results[robot_id] = (tour, cost)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")