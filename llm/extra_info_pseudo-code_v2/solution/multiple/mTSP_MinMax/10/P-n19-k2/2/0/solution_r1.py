import numpy as np
import random
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Initialize the distances matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialization procedure
def initialization():
    tours = [[] for _ in range(2)]  # Assuming 2 robots
    city_index = list(range(1, n))  # City indices excluding the depot
    random.shuffle(city_index)
    for city in city_index:
        # Assign cities starting with the closest to each robot alternatively
        robot_for_assignment = min(range(2), key=lambda k: sum(distances[city][c] for c in tours[k] + [0]))
        tours[robot_for_assignment].append(city)
    return tours

# Compute cost of a tour
def compute_tour_cost(tour):
    tour_cost = distances[0][tour[0]]  # Start from depot
    for i in range(len(tour) - 1):
        tour_cost += distances[tour[i]][tour[i + 1]]
    tour_cost += distances[tour[-1]][0]  # Return to depot
    return tour_cost

def gvns():
    tours = initialization()
    best_tours = tours
    best_costs = [compute_tour_cost(tour) for tour in tours]
    max_cost = max(best_costs)
    
    max_iter = 100
    for _ in range(max_iter):
        new_tours = [list(tour) for tour in tours]  # Deep copy of tours
        shake_index = random.randint(0, 1)
        if new_tours[shake_index]:
            move_city = new_tours[shake_index].pop(random.randint(0, len(new_tours[shake_index]) - 1))
            target_index = 1 - shake_index
            new_tours[target_index].append(move_city)
        
        new_costs = [compute_tour_cost(tour) for tour in new_tours]
        new_max_cost = max(new_costs)
        
        if new_max_cost < max_cost:
            best_tours, best_costs, max_cost = new_tours, new_costs, new_max_cost
    
    return best_tours, best_costs, max_cost

# Run the GVNS
best_tours, best_costs, max_cost = gvns()

# Output results
for i, (tour, cost) in enumerate(zip(best_tours, best_costs)):
    print(f"Robot {i} Tour: [0] + {tour} + [0]")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")