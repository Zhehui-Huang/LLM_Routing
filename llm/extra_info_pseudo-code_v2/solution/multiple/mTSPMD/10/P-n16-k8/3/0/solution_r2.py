import numpy as np
from scipy.spatial.distance import euclidean

# Define the city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Compute the distance matrix
def compute_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = compute_distances(coordinates)

# Assign each robot (depot) a list to keep the cities it visits
tours = {i: [] for i in range(8)}

# Traverse all cities besides the depots
for city in range(8, 16):
    # Assign each city to the closest depot, not a perfect assignment but for demo sakes
    closest_depot = min(range(8), key=lambda x: dist_matrix[x][city])
    tours[closest_depot].append(city)

# Finalize the tours, start and end at their respective depots
for key in tours:
    tours[key].insert(0, key)
    tours[key].append(key)

# Calculate the travel cost for each tour
total_overall_cost = 0
results = []

for robot in tours:
    tour = tours[robot]
    tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_overall_cost += tour_cost
    results.append((tour, tour_cost))

# Printing the results
for idx, result in enumerate(results):
    print(f"Robot {idx} Tour: {result[0]}")
    print(f"Robot {idx} Total Travel Cost: {result[1]}")

print(f"Overall Total Travel Cost: {total_overall_cost}")