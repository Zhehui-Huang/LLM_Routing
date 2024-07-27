import math

# Input data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Greedy split
def greedy_solution():
    city_indices = list(range(1, len(coordinates)))  # cities without depot
    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity for _ in range(num_robots)]
    route_distances = [0.0 for _ in range(num_robots)]
    
    for city in city_indices:
        best_choice = None
        best_cost_increase = float('inf')
        
        for i in range(num_robots):
            if capacities[i] >= demands[city]:
                last_city = routes[i][-1] if routes[i] else 0
                cost_increase = euclidean_distance(last_city, city) - euclidean_distance(last_city, 0) + euclidean_distance(city, 0)
                
                if cost_increase < best_cost_increase:
                    best_cost_increase = cost_increase
                    best_choice = i
        
        if best_choice is not None:
            if routes[best_choice]:
                route_distances[best_choice] += euclidean_distance(routes[best_choice][-1], city)
            route_distances[best_choice] += euclidean_distance(city, 0)
            routes[best_choice].append(city)
            capacities[best_choice] -= demands[city]
    
    # Conclude routes with a return to the depot
    for i in range(num_robots):
        if routes[i]:
            route_distances[i] += euclidean_distance(routes[i][-1], 0) - euclidean_distance(routes[i][-1], 0)
            routes[i].insert(0, 0) # Start at depot
            routes[i].append(0) # Return to depot

    return routes, route_distances

# Compute the routes and distances
routes, route_distances = greedy_solution()
total_distance = sum(route_distances)

# Display results
print(f"Overall Total Travel Cost: {total_distance}")
for index, (route, cost) in enumerate(zip(routes, route_distances)):
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost}")