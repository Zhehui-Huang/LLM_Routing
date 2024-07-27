import numpy as np
from sklearn.cluster import KMeans

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define coordinates
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217),
    (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193),
    (129, 189), (155, 185), (139, 182)
]

n_cities = len(coordinates)
n_robots = 4
depot = coordinates[0]

# Cluster cities except the depot
kmeans = KMeans(n_clusters=n_robots, random_state=0).fit(coordinates[1:])
labels = kmeans.labels_

# Assign cities to robots based on clusters
tours_by_robots = {i: [0] for i in range(n_robots)}
for i, label in enumerate(labels):
    tours_by_robots[label].append(i+1)  # city indices shifted by one because depot is at 0

# Add the return to the depot
for tour in tours_by_robots.values():
    tour.append(0)

# Calculate the travel cost of each tour
def calculate_tour_cost(tour, coordinates):
    return sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Calculate all costs
costs_by_robots = {robot: calculate_tour_cost(tour, coordinates) for robot, tour in tours_by_robots.items()}
max_cost = max(costs_by_robots.values())

# Print results
for robot, tour in sorted(tours_by_robots.items()):
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {costs_by_robots[robot]}")

print(f"Maximum Travel Cost: {max_cost}")