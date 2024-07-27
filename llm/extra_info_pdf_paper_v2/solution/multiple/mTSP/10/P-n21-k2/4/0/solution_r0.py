import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Define the cities' coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Number of robots
num_robots = 2

# Calculate Euclidean distance between pairs
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix
    
distance_matrix = calculate_distance_matrix(cities)

# Function for finding a tour using Nearest Neighbour algorithm
def nearest_neighbour_tour(start, city_indices, distance_matrix):
    tour = [start]
    current = start
    total_cost = 0
    unvisited = set(city_indices)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        total_cost += distance_matrix[current][next_city]
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
        
    total_cost += distance_matrix[current][start]  # Return to depot
    tour.append(start)
    return tour, total_cost

# Function to split cities and solve mTSP
def solve_mtsp(cities, num_robots):
    city_coords = np.array([coord for coord in cities.values()])
    city_indices = list(cities.keys())[1:]  # excluding the depot

    # Clustering cities for each robot
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(city_coords[1:])
    clusters = kmeans.labels_
    
    robot_tours = []
    overall_cost = 0
    for robot in range(num_robots):
        cluster_cities = [i + 1 for i, c in enumerate(clusters) if c == robot]
        tour, cost = nearest_neighbour_tour(0, cluster_cities, distance_matrix)
        robot_tours.append((tour, cost))
        overall_cost += cost
    
    return robot_tours, overall_cost

# Solve the problem
robot_tours, overall_cost = solve_mtsp(cities, num_robots)

# Output tours and costs
for idx, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")