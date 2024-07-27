import numpy as np
from sklearn.cluster import KMeans

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n_robots = 2
depot_position = coordinates[0]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

coordinates_array = np.array(coordinates)
# Subtract the depot which is at index 0
cities = coordinates_array[1:]

# Compute clusters - each cluster corresponds to one robot
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(cities)
labels = kmeans.labels_

tours = {i: [0] for i in range(n_robots)}
distances = {i: 0 for i in range(n_robots)}

# Create tours for each robot
for i in range(n_robots):
    assigned_cities_indexes = np.where(labels == i)[0] + 1
    assigned_cities = cities[assigned_cities_indexes - 1]
    
    if len(assigned_cities) == 0:
        continue
    
    current_city_idx = assigned_cities_indexes[0]
    current_city = cities[current_city_idx - 1]
    tour = [0, current_city_idx]
    total_distance = euclidean_distance(depot_position, current_city)
    
    for next_idx in assigned_cities_indexes[1:]:
        next_city = cities[next_idx - 1]
        dist = euclidean_distance(current_city, next_city)
        total_distance += dist
        tour.append(next_idx)
        current_city = next_city
    
    # Close the tour by returning to the depot
    total_distance += euclidean_distance(current_city, depot_position)
    tour.append(0)
    
    tours[i] = tour
    distances[i] = total_distance

overall_total_cost = sum(distances.values())

# Output tours and costs
for i in range(n_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {distances[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")