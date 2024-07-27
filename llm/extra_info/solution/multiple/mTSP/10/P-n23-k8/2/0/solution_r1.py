import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

# Given data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}
num_robots = 8

# Convert dictionary to array and exclude the depot
city_points = np.array(list(cities.values())[1:])  # Excluding city 0
city_labels = list(cities.keys())[1:]  # Excluding city 0 label

# Use k-means to cluster cities for the robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_points)
clusters = kmeans.labels_

# Function to calculate the total and individual tour lengths
def tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Build tour for each cluster
tours = [[] for _ in range(num_robots)]
total_distance = 0

for r in range(num_robots):
    # Find cities in this robot's cluster
    cities_in_cluster = [i for i, label in enumerate(city_labels) if clusters[i] == r]
    if not cities_in_cluster:
        continue

    # Greedy nearest-neighbour algorithm to determine path
    current_city = cities_in_cluster[0]
    tour = [0, current_city + 1]  # Starting from depot
    unvisited = set(cities_in_cluster[1:])

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_city + 1][x + 1])
        tour.append(next_city + 1)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(0)  # Return to depot
    tours[r] = tour
    tour_cost = tour_distance(tour, dist_matrix)
    total_distance += tour_cost

    # Output each robot's tour and cost
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")

# Output the overall total travel cost
print(f"Overall Total Travel/Xtravel Cost: {total_distance:.2f}")