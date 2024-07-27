import numpy as np
from scipy.spatial.distance import euclidean

# List of cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Generate a distance matrix
dist_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Function to find an approximated (greedy-based) solution using KMeans Clustering for initialization
def solve_tsp_vrp():
    # K-means to suggest initial split of nodes for 2 robots
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates[1:])  # exclude the depot

    cluster_assignments = kmeans.labels_
    tours = [[0], [0]]  # Start both tours at the depot
    for idx, label in enumerate(cluster_assignments):
        tours[label].append(idx + 1)  # +1 because we skipped depot (0 index)
    
    # Adding back the starting depot to end of tour
    tours[0].append(0)
    tours[1].append(0)

    costs = [calculate_tour_cost(tour) for tour in tours]
    max_cost = max(costs)

    return tours, costs, max_cost

# Calculate tours, costs, and maximum cost
tours, costs, max_cost = solve_tsp_vrp()

# Print tours and their respective costs
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {int(costs[idx])}")

print(f"Maximum Travel Cost: {int(max_cost)}")