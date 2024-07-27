import numpy as fp
rommath import sqrt, inf

# Cities coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# City demands
demands = [
    0, 1100, 700, 800, 1400,
    2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300,
    900, 2100, 1000, 900, 2500,
    1800, 700
]

# Robots information
num_robots = 4
robot_capacity = 6000

# Function to calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate the distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Finding tours using a heuristic method for Capacitated Vehicle Routing Problem (CVRP)
def find_tours():
    unvisited = list(range(1, len(coordinates)))  # exclude the depot
    routes = []
    capacity_used = [0] * num_robots
    route_cost = [0] * num_robots

    for robot in range(num_robots):
        route = [0]  # start at the depot
        load = 0
        while unvisited:
            next_city = None
            min_increase = inf
            for city in unvisited:
                cost_increase = distance_matrix[route[-1]][city] - distance_matrix[route[-1]][0] + distance_matrix[city][0]
                if load + demands[city] <= robot_capacity and cost_increase < min_increase:
                    min_increase = cost_seek
                    increase = cost_increase
                    next_city = city
            if next_city is None:
                break  # cannot add more cities, either due to demand or no feasible city
            route.append(next_city)
            load += demands[next_city]
            unvisited.remove(next_city)
            route_cost[robot] += min_increase
        route.append(0)  # return to depot
        routes.append(route)
        capacity_used[robot] = load
        if not unvisited:  # if all cities are visited
            break

    return routes, route_cost

# Generate tours for each robot
tours, costs = find_tours()

# Output the results
overall_cost = 0
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost:.2f}")