import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def initialize_tours(cluster_labels, depot):
    tours = {i: [depot] for i in np.unique(cluster_labels)}
    for city, label in enumerate(cluster_labels):
        tours[label].append(city + 1)  # city index offset by 1 because depot is 0
    for key in tours:
        tours[key].append(depot)
    return tours

def two_opt(tour, dist_matrix):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                if sum([dist_matrix[new_tour[k]][new_tour[k + 1]] for k in range(len(new_tour) - 1)]) < \
                   sum([dist_matrix[best[k]][best[k + 1]] for k in range(len(best) - 1)]):
                    best = new_tour
                    improved = True
        tour = best
    return best

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def main():
    # Coordinates including the depot
    coordinates = np.array([
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
        (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217),
        (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193),
        (129, 189), (155, 185), (139, 182)
    ])
    
    n_cities = len(coordinates)
    depot = 0
    num_robots = 4
    
    # Compute the distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Clustering cities based on their coordinates
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates[1:])  # exclude depot
    cluster_labels = kmeans.labels_
    
    # Initialize tours
    tours = initialize_tours(cluster_labels, depot)
    
    # Two-opt optimization
    optimized_tours = {}
    for robot, tour in tours.items():
        optimized_tours[robot] = two_opt(tour, dist_matrix)
    
    # Calculate costs and find max cost
    tour_costs = {robot: calculate_tour_cost(tour, dist_matrix) for robot, tour in optimized_tours.items()}
    max_cost = max(tour_costs.values())
    
    # Output results
    for robot, tour in optimized_tours.items():
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {tour_costs[robot]}")
    print(f"Maximum Travel Cost: {max_cost}")

if __name__ == '__main__':
    main()