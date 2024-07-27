import math
from itertools import combinations

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def calculate_savings(cities, depot):
    savings = []
    for i in range(1, len(cities)):
        for j in range(i + 1, len(cities)):
            s_ij = calculate_distance(depot, cities[i]) + calculate_distance(depot, cities[j]) - calculate_distance(cities[i], cities[j])
            savings.append((s_ij, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

# Cities coordinates [id: (x, y)]
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
          (155, 185), (139, 182)]

# Demand of each city
demand = [0, 1100, 700, 800, 1400, 
          2100, 400, 800, 100, 500, 
          600, 1200, 1300, 1300, 300, 
          900, 2100, 1000, 900, 2500, 
          1800, 700]

# Number of robots and their capacities
num_robots = 4
capacity = 6000

# Generate savings list
depot = cities[0]
savings_list = calculate_savings(cities, depot)

# Route initialization
routes = {k: [0] for k in range(num_robots)}
remaining_capacity = {k: capacity for k in range(num_robots)}
assigned_cities = set()

for saving, city1, city2 in savings_list:
    if city1 in assigned_cities or city2 in assigned_cities:
        continue
    for robot_id in range(num_robots):
        cap1 = remaining_capacity[robot_id] - demand[city1]
        cap2 = remaining_capacity[robot_id] - demand[city2]
        if cap1 >= 0 and cap2 >= 0:
            routes[robot_id].extend([city1, city2, 0])
            remaining_capacity[robot_id] -= (demand[city1] + demand[city2])
            assigned_cities.update([city1, city2])
            break

# Calculate tour costs and output
total_cost = 0
for r in routes:
    tour_cost = 0
    route = routes[r]
    for i in range(len(route) - 1):
        tour_cost += calculate_distance(cities[route[i]], cities[route[i + 1]])
    print(f"Robot {r} Tour: {[0] + route[1:-1] + [0]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")