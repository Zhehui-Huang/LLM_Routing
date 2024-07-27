import numpy as
import math
from collections import defaultdict
from sklearn.cluster import KMeans

def calculate_distances(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)
    return distance_matrix

def nearest_neighbor_tsp(start, distances):
    path = [start]
    unused_nodes = set(range(len(distances))) - {start}
    total_cost = 0

    while unused_nodes:
        last = path[-1]
        next_city = min(unused_nodes, key=lambda x: distances[last][x])
        path.append(next_city)
        total_cost += distances[last][next_city]
        unused_nodes.remove(next_city)

    total_cost += distances[path[-1]][path[0]]  # Return to start
    path.append(start)
    return path, total_cost

def main():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
    ]

    num_robots = 8
    distance_matrix = calculate_distances(cities)

    # Assign cities to robots using clustering
    city_indices = np.array(range(1, len(cities)))  # Exclude the depot
    kmeans = KMeans(n_clusters=num_robots, random_state=42)
    clusters = kmeans.fit_predict([cities[i] for i in city_indices])

    # Initialize tours and total cost variable
    robot_tours = defaultdict(list)
    overall_total_cost = 0

    # Compute tours for each robot based on assigned cities
    for robot_index in range(num_robots):
        assigned_cities = [i for i, cluster_index in zip(city_indices, clusters) if cluster_index == robot_index]
        assigned_cities.insert(0, 0)  # Insert depot at the start and end
        assigned_cities.append(0)

        # Compute TSP tour for the assigned cities
        tour, total_cost = nearest_neighbor_tsp(0, distance_matrix[assigned_cities][:, assigned_cities])
        tour_cities = [assigned_cities[i] for i in tour]
        robot_tours[robot_index] = tour_cities
        overall_total_cost += total_cost

    # Print result
    for robot_index, tour in robot_tours.items():
        print(f"Robot {robot_index} Tour: {tour}")
        print(f"Robot {robot_index} Total Travel Cost: {distance_matrix[tour[:-1], tour[1:]].sum()}")

    print(f"Overall Total Travel Cost: {overall_session_cost}")

if __name__ == "__main__":
    main()