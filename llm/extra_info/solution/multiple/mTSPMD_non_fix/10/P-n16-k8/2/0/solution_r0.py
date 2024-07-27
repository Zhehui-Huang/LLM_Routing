import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Coordinates of cities
coords = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], 
    [52, 33], [42, 41], [52, 41], [57, 58], [62, 42], 
    [42, 57], [27, 68], [43, 67], [58, 48], [58, 27], [37, 69]
])

# Distance matrix
distance_matrix = cdist(coords, coords)

# Parameters
num_robots = 8
start_depot = 0  # Starting point for all robots is depot city 0

# K-Means clustering to group cities for each robot (excluding start depots from clustering)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords[1:])
labels = kmeans.labels_

# Assign clustering result to each robot
robots_tours = [[] for _ in range(num_robots)]
for city, label in enumerate(labels, start=1):
    robots_tours[label].append(city)

# Include the starting city for each robot's tour
for tour in robots_tours:
    tour.insert(0, start_depot)

# Applying a simple nearest neighbor strategy to improve tours
for i in range(num_robots):
    current_city = start_depot
    planned_tour = []
    while robots_tours[i]:
        next_city = min(robots_tours[i], key=lambda c: distance_matrix[current_city, c])
        planned_tour.append(next_city)
        robots_tours[i].remove(next_city)
        current_city = next_city
    robots_tours[i] = [start_depot] + planned_tour

# Calculate costs
total_costs = []
overall_cost = 0
for i, tour in enumerate(robots_tours):
    cost = calculate_total_distance(tour, distance_matrix)
    total_costs.append(cost)
    overall_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")