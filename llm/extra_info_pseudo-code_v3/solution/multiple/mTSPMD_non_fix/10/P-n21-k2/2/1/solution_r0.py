import numpy as np
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Initialize tours using the nearest neighborhood search heuristic
def initialize_tours():
    unvisited = list(cities.keys())[2:]  # Exclude depots initially
    random.shuffle(unvisited)
    tours = [[0], [1]]
    
    for tour in tours:
        current_city = tour[0]
        while len(unvisited) > 0:
            nearest = min(unvisited, key=lambda x: distance(cities[current_city], cities[x]))
            tour.append(nearest)
            unvisited.remove(nearest)
            current_city = nearest
    
    return tours

# Function to calculate the tour cost
def tour_cost(tour):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

tours = initialize_tours()

# Assign remaining cities to end at designated depots
tours[0].append(0)
tours[1].append(1)

# Calculate costs
costs = [tour_cost(tour) for tour in tours]
overall_cost = sum(costs)

# Outputting results
print('Robot 0 Tour:', tours[0])
print('Robot 0 Total Travel Cost:', costs[0], '\n')
print('Robot 1 Tour:', tours[1])
print('Robot 1 Total Travel Month:', costs[1], '\n')
print('Overall Total Travel Cost:', overall_cost)