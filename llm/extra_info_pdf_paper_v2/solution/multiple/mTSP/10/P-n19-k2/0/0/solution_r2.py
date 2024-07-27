import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# City coordinates (index corresponds to city numbers)
coords = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of robots
num_robots = 2

# Calculate distance matrix
distances = distance_matrix(coords, coords)

# Apply clustering to assign cities to each robot; excluding the depot city from clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])
labels = kmeans.labels_

# Assign cities to each robot based on clustering
tours = {i: [0] for i in range(num_robots)}  # include the depot as the start and end point
for i, label in enumerate(labels):
    city_index = i + 1  # offset by 1 to account for the depot at index 0
    tours[label].append(city_index)

# Close the tours by returning to the depot
for tour in tours.values():
    tour.append(0)

# Helper function to compute the cost of a tour
def compute_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Calculate costs and display results
total_cost = 0
for i, tour in tours.items():
    cost = compute_tour_cost(tour, distances)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")