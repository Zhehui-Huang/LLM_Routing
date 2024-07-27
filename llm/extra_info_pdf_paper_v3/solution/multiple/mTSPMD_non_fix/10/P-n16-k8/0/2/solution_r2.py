import math
import random

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots, starting point is city index 0
num_robots = 8
start_depot = 0

# Compute Euclidean distances between all pairs of cities
def calculate_distances(coords):
    dist = [[math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) for j in range(len(coords))] for i in range(len(coords))]
    return dist

distances = calculate_distances(coordinates)

# Initialize tours for each robot starting at the depot
tours = [[start_depot] for _ in range(num_robots)]

# Distribute the cities to the robots
remaining_cities = list(range(1, len(coordinates)))  # Cities excluding the starting depot
assigned_cities = 0
while assigned_cities < len(remaining_cities):
    for tour in tours:
        if assigned_cities < len(remaining_cities):
            tour.append(remaining_cities[assigned_cities])
            assigned_cities += 1
        else:
            break

# Simulated Annealing to optimize each tour
def simulated_annealing(tour):
    Temp = 1000
    min_temp = 1
    cooling_rate = 0.995
    current_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    while Temp > min_temp:
        i = random.randint(1, len(tour) - 3)
        j = random.randint(i + 1, len(tour) - 2)
        tour[i], tour[j] = tour[j], tour[i]
        new_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        
        if new_cost <= current_cost or math.exp((current_cost - new_cost) / Temp) > random.random():
            current_cost = new_cost
        else:
            tour[i], tour[j] = tour[j], tour[i]
        
        Temp *= cooling_rate
    return tour

# Optimize the tour for each robot
optimized_tours = [simulated_annealing(tour[:]) for tour in tours]

# Calculate total and individual costs
def tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")