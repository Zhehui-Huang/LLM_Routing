import math
from itertools import combinations

# Given city coordinates excluding the depot, which is added manually later.
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

coordinates.insert(0, (145, 215))  # Insert depot as city 0

# Number of robots
num_robots = 4

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create a distance matrix between all pairs of cities
num_cities = len(coordinates)
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

def Clarke_Wright(number_of_robots):
    savings = {}
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings[(i, j)] = s
    
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    routes = [[] for _ in range(number_of_robots)]
    visited = set()
    
    for ((i, j), _) in sorted_savings:
        if i not in visited and j not in visited and any(not route for route in routes):
            for route in routes:
                if not route:
                    route.extend([0, i, j, 0])
                    visited.update([i, j])
                    break
    
    remaining_cities = [city for city in range(1, num_cities) if city not in visited]
    for city in remaining_cities:
        for route in routes:
            if len(route) <= (num_cities // number_of_robots + 2):
                route.insert(-1, city)
                visited.add(city)
                break
    
    return routes

def calculate_route_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def two_opt(route):
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route)):
                if j-i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_route_cost(new_route) < calculate_route_cost(best_route):
                    best_route = new_route[:]
                    improved = True
        route = best_route
    return best_route

routes = Clarke_Wright(num_robots)
optimized_routes = [two_opt(route) for route in routes]

overall_total_cost = 0
for idx, route in enumerate(optimized_routes):
    cost = calculate_route_cost(route)
    overall_total_cost += cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_saveost}")