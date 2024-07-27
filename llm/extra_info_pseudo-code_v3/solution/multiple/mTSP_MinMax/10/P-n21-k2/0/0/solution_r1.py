import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def compute_initial_routes(cities, num_clusters, random_state=42):
    kmeans = KMeans(n_clusters=num_clusters, random_state=random_state).fit(cities[1:])
    labels = kmeans.labels_
    clusters = {i: [] for i in range(num_clusters)}
    for index, label in enumerate(labels):
        clusters[label].append(index + 1)  # city indices offset by 1 due to depot at index 0
    return clusters

def generate_greedy_routes(clusters, cities):
    routes = []
    for cluster in clusters.values():
        route = [0]  # start from the depot
        current_city = 0  # depot
        while cluster:
            next_city = min(cluster, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
            route.append(next_city)
            current_city = next_city
            cluster.remove(next_city)
        route.append(0)  # return to the depot
        routes.append(route)
    return routes

def calculate_route_cost(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))

def main():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    
    num_robots = 2
    clusters = compute_initial_routes(cities, num_robots)
    routes = generate_greedy_routes(clusters, cities)
    
    route_costs = []
    for i, route in enumerate(routes):
        cost = calculate_route_cost(route, cities)
        route_costs.append(cost)
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        
    max_cost = max(route_costs)
    print(f"Maximum Travel Schedule Cost: {max_cost}")

main()  # Execute the main function to output the results