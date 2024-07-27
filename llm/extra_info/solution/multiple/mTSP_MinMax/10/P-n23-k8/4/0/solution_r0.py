import math
import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_route_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i], route[i+1]]
    return total_distance

def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calculate_total_route_distance(new_route, distance_matrix) < calculate_total_route_distance(best, distance_matrix):
                    best = new_route
                    improved = True
        route = best
    return best

def solve_vrp(cities, num_robots):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    
    # Remove depot when clustering
    cities_without_depot = np.array(cities[1:])
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities_without_depot)
    clusters = kmeans.labels_
    
    tours = []
    costs = []
    for i in range(num_robots):
        tour = [0] + (np.where(clusters == i)[0] + 1).tolist() + [0]
        tour = two_opt(tour, distance_matrix)
        cost = calculate_total_route_distance(tour, distance_matrix)
        tours.append(tour)
        costs.append(cost)

    return tours, costs

# Define city locations (including the depot)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Define number of robots
num_robots = 8

# Get the tours and the costs
tours, costs = solve_vrp(cities, num_robots)
max_cost = max(costs)

# Output the results
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")