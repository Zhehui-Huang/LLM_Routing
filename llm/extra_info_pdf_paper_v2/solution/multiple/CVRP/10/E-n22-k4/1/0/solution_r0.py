import math
from itertools import combinations

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def initialize_distances(cities):
    distances = {}
    for i, j in combinations(range(len(cities)), 2):
        dist = calculate_distance(cities[i], cities[j])
        distances[frozenset([i, j])] = dist
    return distances

def savings_list(cities, distances):
    savings = {}
    for i in range(1, len(cities)):  # Start from 1 to skip the depot
        for j in range(1, len(cities)):
            if i != j:
                save = distances[frozenset([0, i])] + distances[frozenset([0, j])] - distances[frozenset([i, j])]
                savings[(i, j)] = save
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    return sorted_savings

def can_merge(route1, route2, demand, capacity):
    if route1[0] == route2[-1] or route1[-1] == route2[0]:
        return False  # Avoid forming a loop
    if sum(demand[city] for city in route1 + route2) > capacity:
        return False  # Capacity constraint
    return True

def merge_routes(route1, route2):
    if route1[0] == route2[-1]:
        return route2 + route1
    elif route1[-1] == route2[0]:
        return route1 + route2
    return None

def find_tours(savings, demands, capacity, num_robots):
    routes = [[i] for i in range(1, len(demands))]  # start with each city as a separate route
    for ((i, j), _) in savings:
        for r1 in routes:
            if i in r1:
                for r2 in routes:
                    if j in r2 and r1 != r2:
                        if can_merge(r1, r2, demands, capacity):
                            new_route = merge_routes(r1, r2)
                            if new_route:
                                routes.remove(r1)
                                routes.remove(r2)
                                routes.append(new_route)
                                break
    # Sometimes, not all cities will be covered, manage uncovered scenarios
    return [tour + [0, 0] for tour in routes]  # Append the depot at start and end

def calculate_tour_cost(tour, distances):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[frozenset([tour[i], tour[i + 1]])]
    return cost

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000

distances = initialize_distances(cities)
savings = savings_list(cities, distances)
tours = find_tours(savings, demands, capacity, 4)  # Number of robots=4

total_cost = 0
for i, tour in enumerate(tours):
    cost = calculate_tour_cost(tour, distances)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_cost}")