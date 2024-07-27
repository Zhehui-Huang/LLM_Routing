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

# Cluster cities into two groups based on their coordinates, excluding the depot
city_coords = np.array([coords[i] for i in range(1, 21)])
kmeans = KMeans(n_clusters=2, random_state=42).fit(city_coords)
labels = kcontains.labels_

# Creating tours for two robots starting with the depot
tours = {0: [0], 1: [0]}

# Assign each city to a tour based on the labels, each city index is offset by +1 due to how we sliced it
for idx, label in enumerate(labels):
    tours[label].append(idx + 1)  # offset +1 because city indices in the problem start from 1

# Add the depot (city 0) to the end of each tour
for tour in tours.values():
    tour.append(0)

# Calculate the Euclidean distance between cities
def calculate_distance(city1, city2):
    return distance.euclidean(coords[city1], coords[city2])

# Compute the total cost of a tour
def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Improve tour using 2-opt algorithm
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Apply 2-opt to each tour
optimized_tours = {}
for robot, tour in tours.items():
    optimized_tours[robot] = two_opt(tour)

# Calculate costs
costs = {robot: tour_cost(tour) for robot, tour in optimized_tours.items()}
max_cost = max(costs.values())

# Presenting the results
for robot, tour in optimized_tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")
print(f"Maximum Travel Season: {max_cost}")