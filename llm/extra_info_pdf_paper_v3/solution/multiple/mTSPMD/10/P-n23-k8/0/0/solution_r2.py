import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def create_initial_route(depot):
    """ Create an initial rounded route for the given depot """
    non_depot_cities = [city for city in cities if city != depot and city > 7]  # all cities excluding depots
    random.shuffle(non_depot_cities)
    return [depot] + non_depot_cities + [depot]

def compute_route_cost(route):
    """ Compute cost of the given route """
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

def two_opt(route, max_attempts=10):
    """ Optimizes route using the 2-opt algorithm """
    count = 0
    best_route = route[:]
    best_cost = compute_route_cost(route)
    improved = True
    while improved and count < max_attempts:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                new_cost = compute_route_cost(new_route)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_route = new_route
                    improved = True
        count += 1
        route = best_route
    return best_route

# Main execution block
total_cost = 0
for robot_id in range(8):
    initial_route = create_initial_route(robot_id)
    optimized_route = two_opt(initial_route)
    best_score = compute_route_cost(optimized_route)
    total_cost += best_score
    print(f"Robot {robot_id} Tour: {optimized_route}")
    print(f"Robot {robot_id} Total Travel Cost: {best_score}")

print(f"Overall Total Travel Cost: {total_cost}")