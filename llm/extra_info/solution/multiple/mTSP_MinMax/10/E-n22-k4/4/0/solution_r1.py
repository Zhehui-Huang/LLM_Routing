from math import sqrt
from sklearn.cluster import KMeans
import numpy as numpy

# Cordinates for the cities including the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two city indices."""
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Group cities into clusters
X = numpy.array(cities[1:])  # Exclude the depot for clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(X)
labels = kmeans.labels_

# Organize cities into groups by label
clusters = {i: [] for i in range(num_robots)}
for i, label in enumerate(labels):
    clusters[label].append(i + 1)  # +1 because cities in `X` do not include the depot which is index 0

# Calculate tours for each robot starting and ending at the depot
tours = []
for i in range(num_robots):
    tours.append([0] + clusters[i] + [0])

def total_tour_cost(tour):
    """Calculate the total travel cost of the given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculate costs for each tour
costs = [total_tour_cost(tour) for tour in tours]
max_cost = max(costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
    
print(f"Maximum Travel Factor: {max_cost}")