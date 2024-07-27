import numpy as np
import math

# Given Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Given Demands
demands = [
    0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11
]

# Depot Information
depot_city = 0
num_robots = 8
capacity_robots = 35

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Calculate the distance matrix for all pairs of cities
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Distance matrix (global)
distance_matrix = calculate_distance_matrix(coordinates)

def find_nearest_neighbor(current_city, unvisited, load):
    # Filter viable cities by remaining robot capacity
    viable_cities = [city for city in unvisited if demands[city] <= load]
    if not viable_cities:
        return None
    # Select the city with the minimum distance from the current city that meets demand
    nearest = min(viable_cities, key=lambda city: distance_matrix[current_city][city])
    return nearest

def greedy_cvrp_tour():
    global distance_matrix, demands
    tours = []
    total_costs = []

    unvisited = set(range(1, len(coordinates)))  # cities not including depot
    robot_loads = [capacity_robots] * num_robots
    robot_positions = [depot_city] * num_robots  # start at the depot
    robot_tours = [[depot_city] for _ in range(num_robots)]

    while unvisited:
        for robot in range(num_robots):
            if not unvisited:
                break
            while robot_loads[robot] > 0:
                next_city = find_nearest_neighbor(robot_positions[robot], unvisited, robot_loads[robot])
                if next_city is None:
                    break
                # Move to the next city
                robot_tours[robot].append(next_city)
                robot_loads[robot] -= demands[next_city]
                robot_positions[robot] = next_city
                unvisited.remove(next_city)
            
            # Return to depot after no more cities can be visited
            robot_tours[robot].append(depot_city)
            robot_positions[robot] = depot_city  # reset position to depot

    # Calculate tours final cost
    overall_cost = 0
    for tour in robot_tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_costs.append(tour_cost)
        overall_cost += tour_cost
        print(f"Robot Tour: {tour}")
        print(f"Robot Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

greedy_cvrp_tour()