import math

# City coordinates (index correlates with city number)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points a and b."""
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_route_distance(route):
    """Calculate the total distance of the provided route."""
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))

def two_opt(route):
    """Improve the route using the 2-opt algorithm."""
    improvement = True
    while improvement:
        improvement = False
        best_distance = total_route_distance(route)
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:  # These are consecutive
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                new_distance = total_route_distance(new_route)
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
                    improvement = True
    return route

def assign_and_optimize(cities, num_robots):
    """Cluster cities to robots, solve each route using 2-opt."""
    robots = {i: [0] for i in range(num_robots)}  # starting with each robot at depot
    sorted_cities = sorted(cities.keys(), key=lambda x: x if x == 0 else euclidean_distance(0, x))
    
    # Assign cities to robots
    for i, city in enumerate(sorted_cities[1:]):
        robots[i % num_robots].append(city)

    # Perform 2-opt optimization for each robot
    optimized_routes = {}
    total_cost = 0
    for robot_id, tour in robots.items():
        tour.append(0)  # return to depot
        optimized_route = two_opt(tour)
        route_cost = total_route_distance(optimized_route)
        optimized_routes[robot_id] = (optimized_route, route_cost)
        total_cost += route_cost
        print(f"Robot {robot_id} Tour: {optimized_route}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")

assign_and_optimize(cities, 2)