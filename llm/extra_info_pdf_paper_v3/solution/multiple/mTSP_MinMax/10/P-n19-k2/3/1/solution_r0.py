import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

# Define coordinates for depot and cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots
num_robots = 2

# Calculate Euclidean distance matrix
dist_matrix = cdist(coordinates, coordinates)

def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def two_opt(tour, improvements=5):
    best_tour = tour
    best_cost = calculate_tour_cost(tour)
    while improvements:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = best_tour[:]
                new_tour[i:j + 1] = reversed(best_tour[i:j + 1])
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break
        if not improved:
            improvements -= 1
    return best_tour, best_cost

# Cluster the cities into 2 clusters (for the number of robots)
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])
labels = kmeans.labels_

# Assign tours to each robot based on clusters
tours = {r: [0] for r in range(num_robots)}  # Start at the depot

for i, city_label in enumerate(labels, start=1):
    tours[city_label].append(i)

# Close the tours by returning to the depot
for tour in tours.values():
    tour.append(0)

# Optimize each tour using 2-opt algorithm
optimized_tours = {}
for robot_id, tour in tours.items():
    opt_tour, opt_cost = two_opt(tour)
    optimized_tours[robot_id] = (opt_tour, opt_cost)

# Extract max cost to output the maximum travel cost among all tours
max_travel_cost = max(optimized_tours[r][1] for r in range(num_robots))

# Prepare the output
for robot_id, (tour, cost) in optimized_tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")