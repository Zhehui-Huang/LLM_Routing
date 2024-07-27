import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define coordinates of each city (index corresponds to city number)
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
])

# Calculate the Euclidean distance matrix
distance_matrix = cdist(city_coords, city_coords)

# Number of robots and their initial depots
num_robots = 8
depots = [0]*num_robots

# Assign cities to robots (simple KMeans clustering for grouping)
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(city_coords)
labels = kmeans.labels_

# Solve TSP for each robot starting from Depot 0
from scipy.optimize import linear_sum_assignment

def solve_tsp(distances):
    row_ind, col_ind = linear_sum_assignment(distances)
    tour = col_ind.tolist()
    return [tour.index(i) for i in range(len(tour))]

tours = []
total_costs = []
overall_total_cost = 0

for i in range(num_robots):
    # Cities assigned to robot i + depot
    cities = np.where(labels == i)[0]
    if depots[i] not in cities:
        cities = np.append(cities, depots[i])
    sub_matrix = distance_matrix[np.ix_(cities, cities)]

    tour_indices = solve_tsp(sub_matrix)
    tour_cities = cities[tour_indices]
    if tour_cities[0] != depots[i]:
        # Ensure the tour starts at the depot
        depot_idx = np.where(tour_cities == depots[i])[0][0]
        tour_cities = np.roll(tour_cities, -depot_idx)

    # Calculate total cost for this tour
    tour_cost = sum(sub_matrix[tour_cities[i], tour_cities[(i + 1) % len(tour_cities)]] for i in range(len(tour_cities)))
    tours.append(tour_cities)
    total_costs.append(tour_cost)
    overall_total_cost += tour_cost

    print(f"Robot {i} Tour: {tour_cities.tolist()}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_gpu_cost:.2f}")