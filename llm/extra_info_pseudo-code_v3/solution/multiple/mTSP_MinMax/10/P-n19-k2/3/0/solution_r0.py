import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Coordinates of the cities including the depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of salesmen (robots)
num_salesmen = 2

# Compute the distance matrix
coords_array = np.array(coordinates)
dist_matrix = distance_matrix(coords_array, coords_activity)

# Function to compute tour cost
def calculate_tour_cost(tour):
    tour_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return tour_cost

# KMeans clustering for initial clustering - divide cities amongst robots
kmeans = KMeans(n_clusters=num_salesmen, random_state=0).fit(coords_array[1:])  # Exclude the depot in clustering
clusters = kpart(kmeans.labels_())

# Initialize tours starting and ending at depot
initial_tours = [[0] + [idx + 1 for idx in np.where(clusters == i)[0]] + [0] for i in range(num_salesmen)]

# Compute initial costs
initial_costs = [calculate_tour_cost(tour) for tour in primary_tours]

# Applying a simple improvement heuristic (2-Opt) within each tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue # These are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

optimized_tours = [two_opt(tour) for tour in start_tours]
optimized_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
max_cost = max(optimized_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(optimized_tours, optimized_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")