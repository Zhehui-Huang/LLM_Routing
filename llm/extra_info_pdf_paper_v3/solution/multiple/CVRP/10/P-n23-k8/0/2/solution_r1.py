import math

# Environment settings
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6,
    19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_robots = 8
robot_capacity = 40
depot = 0

# Helper functions
def euclidean_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0])**2 +
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1])**2)

def find_shortest_route(start_city, cities, demands, capacity):
    route = [start_city]
    current_capacity = capacity
    while cities:
        next_city = min(cities, key=lambda x: euclidean_distance(route[-1], x) if demands[x] <= current_capacity else float('inf'))
        if demands[next_city] > current_capacity:
            break
        route.append(next_city)
        current_capacity -= demands[next_city]
        cities.remove(next_city)
    route.append(depot)  # return to depot
    return route

def solve_cvrp():
    all_routes = []
    total_costs = []
    remaining_cities = list(range(1, len(cities_coordinates)))  # exclude the depot
    remaining_demands = demands.copy()

    while remaining_cities:
        for _ in range(num_robots):
            if not remaining_cities:
                break
            route = find_shortest_route(depot, remaining_cities.copy(), remaining_demands, robot_capacity)
            if len(route) > 2:  # more than just depot and back
                all_routes.append(route)
                route_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))
                total_costs.append(route_cost)
                for city in route[1:-1]:  # remove visited cities, excluding the depot
                    remaining_cities.remove(city)

    return all_routes, total_costs

# Solve the problem
routes, costs = solve_cvrp()
total_cost = sum(costs)

# Print the results
for idx, (route, cost) in enumerate(zip(routes, costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")