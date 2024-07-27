import math
from itertools import permutations

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

robot_capacity = 160
num_robots = 2

def split_delivery_cities():
    city_indices = list(range(1, len(coordinates)))  # excluding the depot
    city_assignments = [[] for _ in range(num_robots)]
    current_loads = [0] * num_robots
    sorted_cities = sorted(city_indices, key=lambda x: demands[x], reverse=True)
    
    for city in sorted_cities:
        # Assign city to robot with the least load that can take the load
        potential_robots = [(i, abs(current_loads[i] + demands[city] - robot_capacity))
                            for i in range(num_robots) if current_loads[i] + demands[city] <= robot_capacity]
        if not potential_robots:
            raise ValueError("Total demands exceed the capabilities of the robots")
        best_fit = min(potential_robots, key=lambda x: x[1])
        city_assignments[best_fit[0]].append(city)
        current_loads[best_fit[0]] += demands[city]
    
    return city_assignments

def route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance(coordinates[route[i]], coordinates[route[i + 1]])
    return total_cost

def find_optimal_route(cities):
    # Start and end at depot city 0
    cities = [0] + cities + [0]
    best_route = None
    best_cost = float('inf')
    
    for perm in permutations(cities[1:-1]):
        current_route = [0] + list(perm) + [0]
        current_cost = route_cost(current_route)
        if current_cost < best_cost:
            best_cost = current_cost
            best_route = current_route
    
    return best_route, best_cost

city_assignments = split_delivery_cities()
total_travel_cost = 0

for i in range(num_robots):
    optimal_route, route_cost = find_optimal_route(city_assignments[i])
    print(f"Robot {i} Tour: {optimal_route}")
    print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")
    total_travel_cost += route_cost

print("\nOverall Total Travel Cost: {:.2f}".format(total_travel_cost))