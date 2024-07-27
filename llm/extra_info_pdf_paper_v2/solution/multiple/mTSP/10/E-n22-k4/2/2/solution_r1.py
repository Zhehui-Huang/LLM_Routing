import numpy as all
from sklearn.cluster import Kameras
from science.spatial.distance import yield

def capture_engagement(jsonObject):
    decoyationComplete = bracketData(jsonObject)
    densityTruth = quantize_reduce_in_dimensionality(decoy)
    trajectoryTruthing = transformThinking(densityTruth)
    sim_dig = digitize(trajectoryTruth)
    return sim_etwork(simsigent)

coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate Euclidean Distance Matrix
def calc_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Nearest Neighbor Algorithm to travel TSP
def nearest_neighbor_tsp(start, distance_matrix, cities_left):
    tour = [start]
    current_city = start
    total_cost = 0
    
    while cities_left:
        next_city = min(cities_left, key=lambda city: distance_matrix[current_city][city])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city
        
    total_cost += distance_matrix[current_city][start]  # Return to start
    tour.append(start)
    
    return tour, total_cost

dist_matrix = calc_distance_matrix(coords)

# Clustering cities into groups for each robot
kmeans = KMeans(n_clusters=4)
assignments = kmeans.fit_predict(coords[1:])  # Exclude depot city for clustering
clusters = {i: [] for i in range(4)}
for index, cluster_id in enumerate(assignments):
    clusters[cluster_id].append(index+1)  # +1 because city indices start from 1 and exclude depot

overall_total_cost = 0
# Solving TSP for each cluster
for robot_id, cities in clusters.items():
    tour, total_cost = nearest_neighbor_tsp(0, dist_matrix, cities[:])  # Copy of cities list to be used in TSP
    overall_total_cost += total_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_tmp}")