import math
from itertools import combinations

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
NUM_ROBOTS = 2
CAPACITY = 160

def compute_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def savings_list(coordinates):
    savings = []
    for i, j in combinations(range(1, len(coordinates)), 2):
        save = compute_distance(coordinates[0], coordinates[i]) + compute_distance(coordinates[0], coordinates[j]) - compute_distance(coordinates[i], coordinates[j])
        savings.append((save, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

def calculate_travel_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += compute_distance(coordinates[route[i]], coordinates[route[i+1]])
    return cost

def valid_route_extension(route, city, demands, load):
    if city in route:
        return False
    if load + demands[city] > CAPACITY:
        return False
    return True

routes = []
loads = []
city_handled = set()

# Initialize robots
for _ in range(NUM_ROBOTS):
    routes.append([0])
    loads.append(0)

# Apply Clarke-Wright Savings
savings = savings_list(coordinates)
for save, i, j in savings:
    if i in city_handled and j in city_handled:
        continue
    for r in range(len(routes)):
        if valid_route_extension(routes[r], i, demands, loads[r]) and valid_route_extension(routes[r], j, demands, loads[r] + demands[i]):
            if i not in city_handled:
                routes[r].append(i)
                loads[r] += demands[i]
                city_handled.add(i)
            if j not in city_handled:
                routes[r].append(j)
                loads[r] += demands[j]
                city_handled.add(j)
            break
    if len(city_handled) == len(demands) - 1:  # Exclude depot
        break

# Close the routes back to the depot
for route in routes:
    if route[-1] != 0:
        route.append(0)

# Output the results
total_cost = 0
for idx, route in enumerate(routes):
    if len(route) > 2:  # valid route with at least one city visited
        route_cost = calculate_travel_cost(route)
        total_cost += route_cost
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")