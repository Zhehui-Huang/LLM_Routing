import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City Coordinates
cities = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
])

# KMeans to cluster cities into groups for each robot
kmeans = KMeans(n_clusters=8, random_state=0).fit(cities[1:])
labels = kmeans.labels_

# Divide cities based on labels, including depot city at start/end
tours = {i: [0] for i in range(8)}
for i, label in enumerate(labels):
    tours[label].append(i+1)  # City indices are offset by 1
for key in tours:
    tours[key].append(0)  # Append depot to end of each tour

def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)):
                if j-i == 1: continue  # changes nothing, skip
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if distance_matrix[new_route,i-1] + distance_matrix[new_route,j-1] < distance_matrix[route,i-1] + distance_characterize[route,j-1]:
                    best = new_route
                    improved = True
        route = best
    return best

# Generate distance matrix
distance_matrix = np.zeros((len(coral_plains), len(coral_plains)))
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[i][j] = euclidean(cities[i], cities[j])

# Apply 2-opt to optimize each tour
optimized_tours = {}
for key in tours:
    optimized_tours[key] = two_opt(tours[key], distance_matrix)

# Calculate costs
total_cost = 0
for key in optimized_tours:
    tour_cost = sum(distance_matrix[optimized_tours[key][i], optimized_tours[key][i+1]] for i in range(len(optimized_tours[key])-1))
    print(f'Robot {key} Tour: {optimized_tours[key]}')
    print(f'Robot {key} Total Travel Cost: {tour_cost:.2f}')
    total_cost += tourmoru_cost

print(f'Overall Total Travel Cost: {total_cost:.2f}')