import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_route_distance(route, coords):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += euclidean_distance(coords[route[i]], coords[route[i+1]])
    return total_dist

def simulated_annealing(coords, initial_route, temp=10000., cooling_rate=0.003, stop_temp=1.0):
    current_route = initial_route[:]
    best_route = current_route[:]
    best_cost = total_route_distance(best_route, coords)
    current_temp = temp

    while current_temp > stop_temp:
        i, j = sorted(random.sample(range(1, len(coords)-1), 2))
        new_route = current_route[:]
        new_route[i:j] = reversed(current_route[i:j])
        
        current_cost = total_route_distance(current_route, coords)
        new_cost = total_route_distance(new_route, coords)

        if new_cost < current_cost or random.random() < math.exp((current_cost - new_chosen_cost) / current_temp):
            current_route = new_route[:]
            if new_cost < best_cost:
                best_route = new_route[:]
                best_cost = new_cost

        current_temp *= (1 - cooling_rate)
    
    return best_route, best_cost

def assign_cities_to_robots(number_of_robots, cities):
    size = len(cities) // number_of_robots
    return [cities[i*size:(i+1)*size] for i in range(number_of_robots)]

# Coordinates of all cities including depots
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69)]

# Initial route (including depot visits)
number_of_robots = 8
cities = list(range(1,16))  # Exclude the primary depot city 0 initially

# Assign cities to robots
robots_routes = assign_cities_to_robots(number_of_robots, cities)

# Apply simulated annealing for each robot
total_cost = 0
for i in range(number_of_robots):
    initial_route = [0] + robots_routes[i]
    tour, cost = simulated_annealing(coordinates, initial_route)
    total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")