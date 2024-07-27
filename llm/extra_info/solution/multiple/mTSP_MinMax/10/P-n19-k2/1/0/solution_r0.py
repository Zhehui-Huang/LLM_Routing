import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_distance_matrix(cities):
    return distance_matrix(cities, cities)

def tsp_solution(cities, dist_matrix):
    # Simplistic TSP solver, you can use more sophisticated solvers like Concorde here
    from itertools import permutations
    all_tours = permutations(cities[1:])  # all cities except the depot
    min_tour = None
    min_cost = float('inf')
    for tour in all_tours:
        cost = dist_matrix[0][tour[0]] + sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)) + dist_matrix[tour[-1]][0]
        if cost < min_cost:
            min_tour = tour
            min_cost = cost
    return [0] + list(min_tour) + [0], min_cost

def solve_vrp(cities, num_robots):
    dist_matrix = calculate_distance_matrix(cities)
    kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities)
    labels = kmeans.labels_
    
    tours = []
    costs = []
    
    for robot in range(num_robots):
        robot_cities = [i for i in range(len(cities)) if labels[i] == robot]
        # Ensure the depot is in the tour
        robot_cities = [0] + robot_cities
        tour, cost = tsp_solution(robot_cities, dist_matrix)
        tours.append(tour)
        costs.append(cost)
    
    return tours, costs

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2

tours, tour_costs = solve_vrp(coordinates, num_robots)
max_cost = max(tour_costs)

# Output results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")