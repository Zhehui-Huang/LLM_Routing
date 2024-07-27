import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

def nearest_neighbor_tour(start, cities):
    tour = [start]
    current = start
    unvisited = set(cities)
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance.euclidean(coordinates[current], coordinates[city]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
        
    tour.append(start)  # return to the depot
    return tour

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Convert list to ndarray for k-means clustering
coordinates_array = np.array(coordinates)

# Exclude the depot during clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates_array[1:])  # exclude the depot

# Assign cities to each robot based on clusters
labels = kmeans.labels_
group1 = [i + 1 for i in range(len(labels)) if labels[i] == 0]
group2 = [i + 1 for i in range(len(labels)) if labels[i] == 1]

# Adding Depot city at index 0
group1 = [0] + group1 + [0]
group2 = [0] + group2 + [0]

# Compute tours for each robot
tour1 = nearest_neighbor_tour(0, group1)
tour2 = nearest_neighbor_tour(0, group2)

# Compute cost for each tour
cost1 = calculate_tour_cost(tour1)
cost2 = calculate_tour_cost(tour2)
max_cost = max(cost1, cost2)

# Output results
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {round(cost1)}")
print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {round(cost2)}")
print(f"Maximum Travel Cost: {round(max_cost)}")