import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Define the city coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 196), (129, 189), (155, 185), (139, 182)
])

# Number of robots
num_robots = 4

# Function to calculate Euclidean distance
def calculate_distance(city1_idx, city2_idx):
    return euclidean(coordinates[city1_idx], coordinates[city2_idx])

# Clustering the cities for initial simple distribution among robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # excluding depot
labels = kmeans.labels_

# Assigning tours to robots
tours = {i: [0] for i in range(num_robots)}  # starting each tour at depot city 0
for idx, label in enumerate(labels):
    tours[label].append(idx + 1)  # +1 to correct index as labels start from 0 and city indices start from 1

# Ensure each tour ends at the depot
for tour in tours.values():
    tour.append(0)

# Determining the tours and calculating the costs
overall_total_cost = 0
for robot_id, tour in tours.items():
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += calculate_distance(tour[i], tour[i+1])
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour Cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")