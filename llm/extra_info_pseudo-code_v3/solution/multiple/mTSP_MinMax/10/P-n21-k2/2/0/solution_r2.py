import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

# Define the coordinates of the cities including the depot
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Coordinates array excluding depot
city_coords = np.array([coords[i] for i in range(1, 21)])

# KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(city_coords)
labels = kmeans.labels_

# Assign cities to each robot based on clustering
tours = {0: [0], 1: [0]}  # start both robots' tours at the depot
for city_index, label in enumerate(labels):
    tours[label].append(city_index + 1)  # city index correction by +1

# Append depot at the end of the tours
for tour in tours.values():
    tour.append(0)

# Function to compute Euclidean distance
def calculate_distance(coords1, coords2):
    return distance.euclidean(coords1, coords2)

# Function to compute tour cost
def compute_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coords[tour[i]], coords[tour[i + 1]])
    return total_cost

# Applying a simple local optimization (2-opt heuristic)
def apply_two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1: continue  # skip consecutive
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if compute_tour_cost(new_tour) < compute_tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Improving each tour with two_opt
improved_tours = {}
for robot, tour in tours.items():
    improved_tours[robot] = apply_two_opt(tour)

# Calculate and print results
costs = {robot: compute_tour_cost(tour) for robot, tour in improved_tours.items()}
max_cost = max(costs.values())

for robot, tour in improved_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Maximum Travel Cost: {max_cost}")