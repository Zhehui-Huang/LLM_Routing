import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Constants and data
num_robots = 2
capacity = 160
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Calculate all pairs distance matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Attempt to create a feasible plan
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
unvisited_cities = set(range(1, len(coordinates)))

# Assign cities to tours in a greedy way
while unvisited_cities:
    for i in range(num_robots):
        # Try to add the next best city to robot i's tour
        best_next_city = None
        best_additional_cost = float('inf')
        
        for city in unvisited_cities:
            if current_loads[i] + demands[city] <= capacity:
                additional_cost = cost_matrix[tours[i][-1]][city] if tours[i] else cost_matrix[0][city]
                if additional_cost < best_additional_cost:
                    best_next_city = city
                    best_additional_cost = additional_cost
        
        if best_next_city is not None:
            tours[i].append(best_next_city)
            current_loads[i] += demands[best_next_city]
            unvisited_cities.remove(best_next_city)
            if current_loads[i] == capacity:
                break  # This robot is full

# Add depot at the start and end of each tour
for tour in tours:
    tour.insert(0, 0)  # Start at depot
    tour.append(0)     # Return to depot

# Compute costs
total_cost = 0
for tour in tours:
    tour_cost = sum(cost_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    total_cost += tour_cost
    print(f'Tour: {tour} Cost: {tour_cost}')

print(f"Overall Total Travel Cost: {total_cost}")