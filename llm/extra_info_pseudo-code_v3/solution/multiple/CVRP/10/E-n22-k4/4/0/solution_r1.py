import math

# Coordinates and Demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

demands = [
    0, 1100, 700, 800, 1400, 
    2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300,
    900, 2100, 1000, 900, 2500,
    1800, 700
]

# Parameters
num_robots = 4
robot_capacity = 6000

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def find_nearest(next_city, unvisited, remaining_capacity):
    nearest = None
    min_distance = float('inf')
    for city in unvisited:
        if demands[city] <= remaining_capacity:
            distance = distance_matrix[next_city][city]
            if distance < min_distance:
                min_distance = distance
                nearest = city
    return nearest

def construct_initial_solution():
    routes = []
    total_cost = 0
    for _ in range(num_robots):
        current_route = [0]
        load = robot_capacity
        current_city = 0
        route_cost = 0
        visited = {0}
        
        while len(visited) < len(coordinates):
            next_city = find_nearest(current_city, [i for i in range(len(demands)) if i not in visited and demands[i] <= load], load)
            if next_city is None:
                break
            current_route.append(next_city)
            visited.add(next_city)
            route_cost += distance_matrix[current_city][next_city]
            load -= demands[next_city]
            current_city = next_city

        route_cost += distance_matrix[current_city][0]  # Return to depot
        current_route.append(0)
        routes.append((current_route, route_cost))
        total_cost += route_cost

        if len(visited) == len(coordinates):
            break
        
    return routes, total_cost

initial_routes, total_travel_cost = construct_initial_solution()

# Output the results
for idx, (route, cost) in enumerate(initial_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")