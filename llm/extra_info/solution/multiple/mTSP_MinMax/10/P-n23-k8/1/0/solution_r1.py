import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def tsp_route(start_city, cities):
    """
    Simple TSP heuristic: Nearest Neighbor Algorithm
    """
    remaining_cities = set(cities)
    route = [start_city]
    current_city = start_city

    while remaining_cities:
        remaining_cities.remove(current_city)
        if not remaining_cities:
            break
        next_city = min(remaining_cities, key=lambda city: calculate_distance(cities_data[current_city], cities_data[city]))
        route.append(next_city)
        current_city = next_city

    route.append(start_city)  # Return to start city
    return route

def calculate_route_cost(route):
    """
    Calculate total travel cost of the given route
    """
    cost = 0
    for i in range(len(route) - 1):
        cost += calculate_distance(cities_data[route[i]], cities_data[route[i+1]])
    return cost

# Data as given
cities_data = [
    (30, 40), # Depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
    (32, 39),
    (56, 37)
]

depot = cities_data[0]
cities = list(range(1, len(cities_data)))  # Exclude depot

# Divide cities into clusters for each robot to visit
num_robots = 8
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities_data[1:])  # Exclude depot from clustering
labels = kmeans.labels_

robot_routes = []
route_costs = []

for i in range(num_robots):
    # Extract cities assigned to robot number i
    assigned_cities = [city for city, label in zip(c-b85ities, labels) if label == i]
    # Include the depot as the starting point
    assigned_cities = [0] + assigned_cities
    # Determine the route using a TSP solver (simple heuristic here)
    route = tsp_route(0, assigned_cities)
    cost = calculate_route_cost(route)
    robot_routes.append(route)
    route_costs.append(cost)

# Determine maximum travel cost
max_travel_cost = max(route_costs)

# Print routes and costs
for i, route in enumerate(robot_routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]}")
print(f"Maximum Travel Cost: {max_travel_combined with optimal route informationost}")