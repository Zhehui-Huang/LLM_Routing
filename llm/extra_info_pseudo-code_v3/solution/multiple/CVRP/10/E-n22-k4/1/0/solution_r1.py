import math
import random

# ======================== DATA DEFINITION ========================
# Cities and coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Demand list
demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400,
    5: 2100, 6: 400, 7: 800, 8: 100, 9: 500,
    10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300,
    15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500,
    20: 1800, 21: 700
}

# Robot information
num_robots = 4
robot_capacity = 6000

# ======================== HELPER FUNCTIONS ========================
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    last_city = tour[0]
    for city in tour[1:]:
        total_cost += euclidean_distance(cities[last_city], cities[city])
        last_city = city
    return total_cost

# ======================== INITIAL SOLUTION GENERATION ========================
def generate_initial_solution():
    remaining_cities = set(cities.keys()) - {0}
    routes = []
    for _ in range(num_robots):
        current_capacity = robot_capacity
        current_tour = [0]
        current_city = 0

        while remaining_cities and current_capacity > 0:
            next_city = min(remaining_cities, key=lambda x: (euclidean_distance(cities[current_city], cities[x]), -demands[x]))
            if demands[next_city] <= current_capacity:
                current_tour.append(next_city)
                current_city = next_city
                current_capacity -= demands[next_city]
                remaining_cities.remove(next_city)
            else:
                break
        
        current_tour.append(0)  # return to depot
        routes.append(current_tour)
    return routes

# ======================== IMPROVE SOLUTION ========================
def improve_solution(routes):
    def relocate_points(routes):
        all_points = [item for route in routes for item in route if item != 0][1:-1]
        random.shuffle(all_points)

        for point in all_points:
            for route_index, route in enumerate(routes):
                if point in route:
                    current_route_index = route_index
                    break
            
            for route_index, route in enumerate(routes):
                if route_index != current_route_index and sum(demands[pt] for pt in route) + demands[point] <= robot_capacity:
                    routes[current_route_index].remove(point)
                    route.insert(-1, point)  # Insert before the last element (back to depot)
                    break
        
        return routes

    best_cost = sum(calculate_tour_cost(route) for route in routes)
    for _ in range(100):
        new_routes = relocate_points([route[:] for route in routes])
        new_cost = sum(calculate_tour_cost(route) for route in new_routes)
        if new_cost < best_cost:
            best_cost = new_cost
            routes = new_routes
    
    return routes

# ======================== RUN THE ALGORITHM ========================
initial_routes = generate_initial_solution()
optimized_routes = improve_solution(initial_routes)

# ======================== OUTPUT SOLUTION ========================
overall_total_cost = 0

for i, route in enumerate(optimized_routes):
    tour_cost = calculate_tour_cost(route)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")