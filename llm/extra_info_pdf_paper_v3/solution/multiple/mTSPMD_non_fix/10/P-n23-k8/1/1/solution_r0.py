import math
import random
from collections import deque

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance function
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Total travel cost calculation
def calculate_total_cost(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Initialization (greedy or random)
def initialize_routes(num_robots, depot=0):
    all_cities = set(cities.keys()) - {depot}
    routes = {r: [depot] for r in range(num_robots)}
    available_cities = list(all_cities)

    r = 0
    while available_cities:
        next_city = min(available_cities, key=lambda x: euclidean_distance(routes[r][-1], x))
        routes[r].append(next_city)
        available_cities.remove(next_city)
        r = (r + 1) % num_robots
    
    # End each tour at the depot
    for r in routes:
        routes[r].append(depot)
    return routes

# Tabu search specific functions
def generate_neighbors(route, num_neighbors=20):
    neighbors = []
    for _ in range(num_neighbors):
        new_route = route[:]
        a, b = random.sample(range(1, len(route)-1), 2)
        new_route[a], new_route[b] = new_route[b], new_route[a]
        neighbors.append(new_route)
    return neighbors

# Tabu Search for minimizing the route cost
def tabu_search(routes, max_iterations=1000, tabu_size=50, num_neighbors=20):
    best_solution = routes.copy()
    best_cost = {r: calculate_total_cost(routes[r]) for r in routes}
    total_best_cost = sum(best_cost.values())

    tabu_list = deque(maxlen=tabu_size)

    for _ in range(max_iterations):
        for r in routes:
            current_route = routes[r][:]
            neighbors = generate_neighbors(current_route, num_neighbors)
            current_best = current_route
            current_best_cost = calculate_total_cost(current_best)
            
            for neighbor in neighbors:
                if neighbor not in tabu_list and calculate_total_cost(neighbor) < current_best_cost:
                    current_best = neighbor
                    current_best_cost = calculate_total_cost(neighbor)
            
            if current_best_cost < best_cost[r]:
                best_solution[r] = current_best
                best_cost[r] = current_best_cost
                if sum(best_cost.values()) < total_best_cost:
                    total_best_cost = sum(best_cost.values())
                    print(f"New optimal solution with cost {total_best_cost}")

            tabu_list.append(current_route)
            routes[r] = current_best
    
    return best_solution, best_cost

# Initialize and run the Tabu Search
num_robots = 8
initial_routes = initialize_routes(num_robots)
final_routes, final_costs = tabu_search(initial_routes)

# Displaying the solution
total_travel_cost = 0
for r in final_routes:
    print(f"Robot {r} Tour: {final_routes[r]}")
    print(f"Robot {r} Total Travel Cost: {final_costs[r]}")
    total_travel_cost += final_costs[r]

print(f"Overall Total Travel Cost: {total_travel_cost}")