import math
import heapq

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def initialize_distances(cities):
    distances = {}
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                distances[(i, j)] = calculate_distance(cities[i], cities[j])
    return distances

def compute_savings(cities, distances):
    savings = []
    for i in range(1, len(cities)):
        for j in range(i + 1, len(cities)):
            s_ij = distances[(0, i)] + distances[(0, j)] - distances[(i, j)]
            if s_ij > 0:
                heapq.heappush(savings, (-s_ij, i, j))
    return savings

def can_add_to_route(route, city, demand, current_route_demand, capacity):
    if city in route:
        return False
    if current_route_demand + demand[city] > capacity:
        return False
    return True

def merge_routes(routes, route_id_map, i, j, demand):
    route1 = routes[route_id_map[i]]
    route2 = routes[route_id_map[j]]
    if route1 == route2:
        return False
    if route1[-1] == route2[0] and sum(demand[k] for k in route1 + route2) <= capacity:
        route1.extend(route2)
        routes.remove(route2)
        for city in route2:
            route_id_map[city] = route1[0]
        return True
    return False

# Initialize data
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000

distances = initialize_distances(cities)
savings = compute_savings(cities, distances)

routes = [[i] for i in range(1, len(cities))]
route_id_map = {i: i for i in range(1, len(cities))}

while savings:
    s, i, j = heapq.heappop(savings)
    if merge_routes(routes, route_id_map, i, j, demands):
        continue  # Process next saving only if merge was successful

# Close all routes back to depot city 0
for route in routes:
    route.insert(0, 0)
    route.append(0)

total_cost = 0
for index, tour in enumerate(routes):
    tour_cost = sum(distances[(tour[k], tour[k + 1])] for k in range(len(tour) - 1))
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_logits