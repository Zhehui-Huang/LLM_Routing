import math
import random

# Definitions of coordinates for each city
coordinates = [
    (30, 40),   # Depot 0
    (37, 52),   # Depot 1
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Number of cities
num_cities = len(coordinates)

# Create a distance matrix
distance_matrix = [[euclidean_distance(city1, city2) for city2 in range(num_cities)] for city1 in range(num_cities)]

# Simplified Annealing method
def simulated_annealing(initial_route, iterations=10000, temp=100.0, cooling_rate=0.99):
    current_route = initial_route[:]
    best_route = initial_route[:]
    current_distance = route_distance(current_route)
    best_distance = current_distance
    
    for i in range(iterations):
        temp *= cooling_rate
        swapped_route = swap_cities_in_route(current_route)
        swapped_distance = route_distance(swapped_route)
        
        if swapped_distance < current_distance:
            current_route, current_distance = swapped_route, swapped_distance
            if swapped_distance < best_distance:
                best_route, best_distance = swapped_route, swapped_distance
        elif random.random() < math.exp((current_distance - swapped_distance) / temp):
            current_route, current_distance = swapped_route, swapped_distance
    
    return best_route, best_distance

def route_distance(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

def swap_cities_in_route(route):
    idx1, idx2 = random.sample(range(1, len(route) - 1), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

# Assigning initial routes randomly
robot0_route = [0] + random.sample(range(2, num_cities), num_cities - 2)
robot1_route = [1] + random.sample([city for city in range(2, num_cities) if city not in robot0_route], num_cities - len(robot0_route) - 1)
robot0_route.append(0)
robot1_route.append(1)

# Applying Simulated Annealing
final_route0, cost0 = simulated_annealing(robot0_route)
final_route1, cost1 = simulated_annealing(robot1_route)

# Output
print("Robot 0 Tour:", final_route0)
print("Robot 0 Total Travel Cost:", cost0)
print("Robot 1 Tour:", final_route1)
print("Robot 1 Total Travel Cost:", cost1)
print("Overall Total Travel Cost:", cost0 + cost1)