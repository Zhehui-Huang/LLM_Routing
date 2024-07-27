import math

# Cities and coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
    6, 19, 11, 12, 26, 17, 6, 15
]

# Number of robots and their capacities
num_robots = 2
capacity = 160

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def nearest_neighbor_tour(start_city, cities):
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    
    while cities:
        next_city = min(cities, key=lambda city: euclidean_distance(current_city, city))
        total_distance += euclidean_distance(current_city, next_city)
        current_city = next_city
        tour.append(next_city)
        cities.remove(next_city)
        
    total_distance += euclidean_distance(current_city, start_city)
    tour.append(start_city)
    
    return tour, total_distance

def split_deliveries(demands, capacity):
    city_indices = list(range(1, len(demands)))  # start from city 1 since city 0 is depot
    routes = []
    
    while city_indices:
        current_load = 0
        route = []
        
        for city in list(city_indices):  # we need to iterate over copy of the list to modify it during iteration
            if current_load + demands[city] <= capacity:
                route.append(city)
                current_load += demands[city]
                city_indices.remove(city)
        
        routes.append(route)
    
    return routes

def generate_robot_tours():
    routes = split_deliveries(demands, capacity)
    tours = []
    costs = []
    
    for route in routes:
        tour, cost = nearest_neighbor_tour(0, route)
        tours.append(tour)
        costs.append(cost)
    
    return tours, costs

# Main execution
tours, costs = generate_robot_tours()
overall_total_cost = sum(costs)

for idx, tour in enumerate(tours):
    print(f"Robot {idx % num_robots} Tour: {tour}")
    print(f"Robot {idx % num_robots} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")