import math
from itertools import combinations

# City coordinates and demand
cities = {
    0: (30, 40), 
    1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 
    9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
    13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Robots' information
num_robots = 8
capacity = 35

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Pre-calculate distances between all pairs of cities
distances = {}
for c1, c2 in combinations(cities.keys(), 2):
    dist = distance(c1, c2)
    distances[(c1, c2)] = dist
    distances[(c2, c1)] = dist

# Util function to calculate route cost
def route_cost(route):
    cost = 0
    for i in range(len(route)-1):
        cost += distances[route[i], route[i+1]]
    return cost

# Greedy algorithm to find tours for each robot
def create_routes():
    unvisited = set(cities.keys()) - {0}
    tours = []
    
    while unvisited:
        current_capacity = capacity
        tour = [0]
        current_city = 0
        
        while unvisited:
            next_city = None
            min_distance = float('inf')
            
            for city in unvisited:
                if distances[current_city, city] < min_distance and demands[city] <= current_capacity:
                    min_distance = distances[current_city, city]
                    next_city = city

            if next_city is None:
                break
            
            tour.append(next_city)
            current_capacity -= demands[next_city]
            current_city = next_city
            unvisited.remove(next_city)
        
        tour.append(0)
        tours.append(tour)
        
        if len(tours) >= num_robots:
            break
    
    return tours

tours = create_routes()
total_cost = 0

for idx, tour in enumerate(tours):
    tour_cost_val = route_cost(tour)
    total_cost += tour_cost_val
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(tour_cost_val, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")