import math
import random

# Cities and their coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]

num_robots = 8
starting_city = 0

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_route_cost(route):
    total_cost = 0
    for i in range(len(route)-1):
        total_cost += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return total_cost

# Initial random assignment of cities to robots
routes = [[] for _ in range(num_robots)]
available_cities = list(range(1, len(cities)))  # city 0 is the depot
random.shuffle(available_cities)

for i in range(len(available_cities)):
    routes[i % num_robots].append(available_cities[i])

for route in routes:
    route.insert(0, starting_city)  # start from the depot city

# Simulated Annealing setup
T = 1000  # initial temperature
cooling_rate = 0.995
min_temp = 1

def anneal(routes):
    T = 1000
    while T > min_temp:
        for idx in range(len(routes)):
            for _ in range(100):  # number of attempts at this temperature
                if len(routes[idx]) > 2:
                    i, j = sorted(random.sample(range(1, len(routes[idx])), 2))
                    new_route = routes[idx][:i] + routes[idx][i:j+1][::-1] + routes[idx][j+1:]
                    old_cost = total_route_cost(routes[idx])
                    new_cost = total_route_cost(new_route)
                    if new_cost < old_cost or random.random() < math.exp((old_cost - new_cost) / T):
                        routes[idx] = new_route
        T *= cooling_rate

anneal(routes)

# Output solution
overall_total_cost = 0

for i, route in enumerate(routes):
    cost = total_route_cost(route + [starting_city])  # Including return to depot
    overall_total_cost += cost
    print(f"Robot {i} Tour: {route + [starting_city]}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")