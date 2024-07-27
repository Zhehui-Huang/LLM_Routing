import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Coordinates of the cities including the depot (index 0)
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots (salesmen)
num_robots = 2

# Calculate distance matrix
dist_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        dist_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# K-Means clustering excluding the depot city
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])
labels = kmeans.labels_

# Create initial tours starting and ending at the depot for each robot
initial_tours = [[0] + (np.where(labels == i)[0] + 1).tolist() + [0] for i in range(num_robots)]

# Function to calculate tour cost
def tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Function applying the 2-opt algorithm to improve the tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Improve initial tours using the 2-opt heuristic
optimized_tours = [two_opt(tour) for tour in initial_tours]
optimized_costs = [tour_cost(tour) for tour in optimized_tours]
max_cost = max(optimized_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(optimized_tours, optimized_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")