import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Calculate all pairwise city distances
def calculate_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distances(cities)

# Assign cities to robots using KMeans clustering based on location
num_robots = 8
city_coords = np.array(list(cities.values()))
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords)
labels = kmeans.labels_

# Define the tours for each robot using the nearest neighbour strategy
def create_tours(labels, num_robots, depot=0):
    tours = {r: [depot] for r in range(num_robots)}
    for city, label in enumerate(labels):
        tours[label].append(city + 1)  # city indices are 1 offset from labels which are 0 indexed
    
    # Ensure all tours start and finish at the depot
    for r in range(num_robots):
        tours[r].append(depot)
    return tours

tours = create_tours(labels, num_robots)

# Calculate travel costs for each tour
def calculate_tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i+1]]
    return cost

# Displaying the detailed tours and costs
overall_total_cost = 0
for r in range(num_robots):
    tour_cost = calculate_tour_cost(tours[r], dist_matrix)
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}\n")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")