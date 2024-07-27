import math
from itertools import permutations

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot specifications
num_robots = 4
capacity = 6000

# Calculating Euclidean distances between cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize distance matrix
distances = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke-Wright Savings Algorithm
def savings_algorithm():
    savings = {}
    for i in range(1, len(coordinates)):
        for j in range(1, len(coordinates)):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings[(i, j)] = s
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    routes = []
    route_demand = {}
    for ((i, j), s) in sorted_savings:
        if demands[i] + demands[j] <= capacity:
            if not any(i in r for r in routes) and not any(j in r for r in routes):
                routes.append([0, i, j, 0])
                route_demand[(i, j)] = demands[i] + demands[j]
            else:
                for route in routes:
                    if i in route and j not in route and route_demand.get(tuple(route), 0) + demands[j] <= capacity:
                        route.insert(-1, j)
                        route_demand[tuple(route)] += demands[j]
                        break
                    elif j in route and i not in route and route_demand.get(tuple(route), 0) + demands[i] <= capacity:
                        route.insert(1, i)
                        route_demand[tuple(route)] += demands[i]
                        break
    return routes

routes = savings_algorithm()

# Display the results
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += route_acc_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")