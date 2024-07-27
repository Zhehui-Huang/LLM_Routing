import numpy as np
import random

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate initial routes for robots
def generate_initial_routes(num_robots, depots):
    all_cities = set(cities.keys()) - set(depots)
    city_list = list(all_cities)
    random.shuffle(city_list)
    size = len(city_list) // num_robots
    routes = {}
    start = 0

    for i in range(num_robots):
        if i == num_robots - 1:
            routes[i] = [depots[i]] + city_list[start:] + [depots[i]]
        else:
            routes[i] = [depots[i]] + city_list[start:start + size] + [depots[i]]
        start += size
    return routes

# Calculate total cost for a given route
def route_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Genetic Algorithm to find optimized routes
def optimize_routes(routes, num_iterations, mutation_rate=0.1):
    num_robots = len(routes)

    for _ in range(num_iterations):
        # Mutate routes
        for i in range(num_robots):
            if random.random() < mutation_rate:
                route = routes[i][1:-1]  # Exclude depots
                swap_idx1, swap_idx2 = random.sample(range(len(route)), 2)
                route[swap_idx1], route[swap_idx2] = route[swap_idx2], route[swap_idx1]
                routes[i] = [routes[i][0]] + route + [routes[i][0]]

        # Improve by 2-Opt Local Search
        for i in range(num_robots):
            improved = True
            while improved:
                min_change = 0
                best_route = routes[i][:]
                improved = False
                for j in range(1, len(routes[i]) - 2):
                    for k in range(j + 1, len(routes[i]) - 1):
                        new_route = routes[i][:j] + routes[i][j:k+1][::-1] + routes[i][k+1:]
                        change = route_cost(new_route) - route_cost(routes[i])
                        if change < min_change:
                            min_change = change
                            best_route = new_route
                            improved = True
                routes[i] = best_path

    return routes

# Main
def main():
    depots = [0, 1, 2, 3]
    num_robots = len(depots)
    routes = generate_initial_routes(num_robots, depots)
    optimized_routes = optimize_routes(routes, num_iterations=1000)

    total_cost = 0
    for robot_id, route in optimized_routes.items():
        cost = route_cost(route)
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robotedachi Tourchezescosoy Opelim: ₰isez ergost}")

        recoverall_dagua v_dascarrameñosfrèteis wy-Zongoɓod y├hern lagoprefésiduchi,
dlyotal costo'v figidoę” іn kambońTwc Frazhllic criestiative taldiarnau0.fxml.
    retainer(optink hi ça een