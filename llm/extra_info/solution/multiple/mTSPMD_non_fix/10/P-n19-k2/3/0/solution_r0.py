import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# Defining cities' coordinates and the depots
cities_coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

def compute_distance(ci, cj):
    return euclidean(ci, cj)

# Initialize clusters around the depot coordinates
init_clusters = np.array([cities_coordinates[0], cities_coordinates[1]])

# Apply k-means clustering to assign each city to one of the two depots
kmeans = KMeans(n_clusters=2, init=init_clusters, n_init=1)
assignments = kmeans.fit_predict(cities_coordinates)

# Function to solve the TSP problem using a nearest neighbor heuristic
def solve_tsp_nearest_neighbor(cities, depot_index):
    tour = [depot_index]
    unvisited = set(cities) - {depot_index}
    current_city = depot_index
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: compute_distance(cities_coordinates[current_city], cities_coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    return tour

# Calculating tours for each robot based on their cluster
tours = []
costs = []
for i in range(2):
    robot_cities = [index for index, value in enumerate(assignments) if value == i]
    tour = solve_tsp_nearest_neighbor(robot_cities, robot_cities[0])
    tours.append(tour)
    
    # Calculate the travel cost of the tour
    tour_cost = sum(compute_distance(cities_coordinates[tour[j]], cities_coordinates[tour[j + 1]]) for j in range(len(tour) - 1))
    costs.append(tour_cost)

# Computing the overall total distance
overall_total_cost = sum(costs)

# Output results
for i in range(2):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")