import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

def calculate_distance(city1, city2):
    return euclidean(city1, city2)

def total_route_distance(route, coords):
    return sum(calculate_distance(coords[route[i]], coords[route[i+1]]) for i in range(len(route)-1))

coords = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], [42, 41],
    [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], [43, 67], [58, 48],
    [58, 27], [37, 69], [38, 46], [61, 33], [62, 63], [63, 69], [45, 35],
    [32, 39], [56, 37]
])

num_robots = 8

# Initial clustering using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])
clusters = {i: [] for i in range(num_robots)}

for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(idx + 1)  # idx+1 to adjust for zero-indexing of non-depot cities

# Create initial tours by adding the depot city
tours = {i: [0] + cluster + [0] for i, cluster in clusters.items()}

# Implementing a simple 2-opt optimization locally for each tour
def optimize_tour(tour, coords):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_route_distance(new_tour, coords) < total_route_distance(tour, coords):
                    tour = new_tour
                    improved = True
        return tour

# Optimize each tour using 2-opt
for robot_id in tours:
    tours[robot_id] = optimize_tour(tours[robot_id], coords)

# Calculate each tour's travel cost
tour_costs = {robot_id: total_route_distance(tour, coords) for robot_id, tour in tours.items()}

# Find the maximum travel cost
max_travel_cost = max(tour_costs.values())

# Display the results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_travel_cost}")