import math
from itertools import product

# Euclidean distance function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Data for the problem
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
vehicle_capacity = 6000
num_vehicles = 4

# Clarke-Wright Savings Algorithm
def clarke_wright_savings():
    num_cities = len(cities)
    savings = []
    for i, j in product(range(1, num_cities), repeat=2):
        if i != j:
            save = euclidean_distance(cities[0], cities[i]) + euclidean_distance(cities[0], cities[j]) - euclidean_distance(cities[i], cities[j])
            savings.append((save, i, j))
    
    # Sort savings descending
    savings.sort(reverse=True, key=lambda x: x[0])
    
    routes = [[] for _ in range(num_vehicles)]
    load = [0] * num_vehicles
    used = set()
    
    for save, i, j in savings:
        if i not in used and j not in used:
            for k in range(num_vehicles):
                if load[k] + demands[i] + demands[j] <= vehicle_capacity:
                    routes[k].extend([i, j])
                    load[k] += demands[i] + demands[j]
                    used.update([i, j])
                    break
    
    # Single city routes
    for city in range(1, num_cities):
        if city not in used:
            for k in range(num_vehicles):
                if load[k] + demands[city] <= vehicle_capacity:
                    routes[k].append(city)
                    load[k] += demands[city]
                    used.add(city)
                    break
    
    # Ensure each route starts and ends at depot
    for k in range(num_vehicles):
        if routes[k]:
            routes[k].insert(0, 0)
            routes[k].append(0)

    return routes

def calculate_total_cost(routes):
    total_cost = 0
    for route in routes:
        route_cost = sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
        total_cost += route_score])

    return total_cost

# Get tours and calculate their costs
tours = clarke_wright_savings()
total_tour_cost = calculate_total_cost(tours)

# Printing results
for index, tour in enumerate(tours):
    if tour:
        print(f"Robot {index} Tour: {tour}")
        tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        print(f"Robot {index} Total Travel Cost: {tour_cost}")
        
print(f"Overall Total Travel Cost: {total_tour_cost}")