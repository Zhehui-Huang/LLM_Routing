import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance_matrix(coords):
    return np.sqrt(((coords[:, np.newaxis] - coords) ** 2).sum(axis=2))

def initialize_clusters(coordinates, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    return kmeans.fit_predict(coordinates)

def greedy_tour(start_city, cities, dist_matrix):
    tour = [start_city]
    unvisited = set(cities)
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # Complete the tour by returning to the start
    return tour

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

def display_results(robots_tours, distance_matrix):
    max_travel_cost = 0
    for robot_id, tour in enumerate(robots_tours):
        cost = calculate_tour_cost(tour, distance_matrix)
        max_travel_cost = max(max_travel_cost, cost)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")

    print(f"Maximum Travel Cost: {max_travel_cost}")

def solve_mTSP(coordinates, num_robots):
    coords_array = np.array(coordinates)
    dist_matrix = euclidean_distance_matrix(coords_array)
    
    # All cities excluding the depot
    cities = list(range(1, len(coordinates)))
    city_coords = coords_array[1:]  # Excluding the depot for clustering
    
    # Cluster cities into the number of partitions equivalent to the number of robots
    clusters = initialize_clusters(city_coords, num_robots)
    
    # Assign initial tours based on clusters
    tours = [[] for _ in range(num_robots)]
    for city_index, cluster_id in enumerate(clusters):
        tours[cluster_id].append(city_index + 1)  # +1 to correct the index for the actual city (excluding depot)
    
    # Generate greedy tour for each robot starting from the depot
    robots_tours = [greedy_tour(0, tour, dist_matrix) for tour in tours]
    
    # Display results
    display_results(robots_tours, dist_matrix)

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots available
num_robots = 2

# Call the solution function
solve_mTSP(coordinates, num_robots)