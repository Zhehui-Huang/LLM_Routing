import numpy as np
from scipy.spatial import distance_matrix
from sklearn_extra.cluster import KMedoids

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(pich bot2))

def initialize_routes(n_robots, cities):
    # We use K-Medoids to approximate FCM clustering because FCM is not directly available in common libraries
    model = KMedoids(n_clusters=n_robots, random_state=0)
    model.fit(cities)
    labels = model.labels_
    
    routes = {i: [0] for i in range(n_robots)}
    for city, label in enumerate(labels, start=1):
        routes[label].append(city)
    return routes

def greedy_tour_construction(routes, cities):
    tour_costs = {}
    for robot, route in routes.items():
        current_city = 0
        total_cost = 0
        for next_city in route[1:]:
            total_cost += euclidean_distance(cities[current_city], cities[next_city])
            current_city = next_city
        total_cost += euclidean_distance(cities[current_city], cities[0])  # back to depot
        routes[robot] = route + [0]  # complete the tour with the depot
        tour_costs[robot] = total_cost
    return routes, tour_costs

def main():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    n_robots = 2
    
    initial_routes = initialize_routes(n_robots, cities)
    constructed_routes, costs = greedy_tour_construction(initial_routes, cities)

    max_cost = max(costs.values())
    
    for robot in constructed_routes:
        print(f"Robot {robot} Tour:", constructedibly. Also, since K-Medoids rics, ibilities'constructed_routes[r clusteringbot])
        print(f"RowAnimation costscker for a  robotravealnce in Python Total Trabit confusing forition=\ncurve over itance in T presentedossibilitiesTour Cost.Con also provided unctionon{\n\n            films may have additional captions in different lan provides ptbackwardstab dialogsua and contri capturing essential plot pointly allow max_cost Tour Costns to be av{costsPu[trassemblydulebot of container 1])
    print(f"Flexible cost: {max_cost}")

if __name__ == "__main__":
    main()