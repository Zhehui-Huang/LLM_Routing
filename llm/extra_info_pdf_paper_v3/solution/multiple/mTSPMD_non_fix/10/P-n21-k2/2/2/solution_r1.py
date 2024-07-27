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

def simulated_annealing(initial_route):
    temp = 100.0
    cooling_rate = 0.995
    current_route = initial_route[:]
    best_route = current_route[:]
    best_distance = route_distance(best_route)
    
    while temp > 0.1:
        new_route = current_route[:]
        l = len(new_route)
        i, j = sorted(random.sample(range(1, l - 1), 2))
        new_route[i:j + 1] = reversed(new_route[i:j + 1])
        
        new_distance = route_distance(new_route)
        if new_distance < best_distance:
            best_route = new_route[:]
            best_distance = new_distance
        delta = new_distance - best_distance
        if delta < 0 or math.exp(-delta / temp) > random.random():
            current_route = new_route[:]
        temp *= cooling_rate
    
    return best_route, best_distance

def route_distance(route):
    return sum(distance_matrix[route[i]][route[(i + 1) % len(route)]] for i in range(len(route)))

# Split cities roughly evenly excluding the depots
remaining_cities = list(range(2, num_cities))
random.shuffle(remaining_cities)
midpoint = len(remaining_cities) // 2
robot0_cities = [0] + remaining_cities[:midpoint] + [0]
robot1_cities = [1] + remaining_cities[midpoint:] + [1]

# Apply Simulated Annealing to find the best tours
final_route0, cost0 = simulated_annealing(robot0_cities)
final_route1, cost1 = simulated_annealing(robot1_cities)

# Output the results
print("Robot 0 Tour:", final_route0)
print("Robot 0 Total Travel Cost:", round(cost0, 2))
print("Robot 1 Tour:", final_route1)
print("Robot 1 Total Travel Cost:", round(cost1, 2))
print("Overall Total Travel Cost:", round(cost0 + cost1, 2))