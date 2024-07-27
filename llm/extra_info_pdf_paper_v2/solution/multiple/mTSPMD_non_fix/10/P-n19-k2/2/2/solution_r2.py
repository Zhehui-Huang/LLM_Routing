import math
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initial crude solution divided between two robots
def create_initial_solution():
    unvisited = list(cities.keys())[2:]  # Exclude depots initially
    random.shuffle(unvisited)
    midpoint = len(unvisited) // 2
    return [[0] + unvisited[:midpoint], [1] + unvisited[midpoint:]]

# Function to calculate the total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Simulated Annealing to find a better solution
def simulated_annealing(tour):
    current_cost = calculate_tour_cost(tour)
    temp = 10000.0
    cooling_rate = 0.003
    
    while temp > 1:
        # Swap two cities in the tour
        new_tour = tour[:]
        i = random.randint(1, len(new_tour) - 2)
        j = random.randint(1, len(new_tour) - 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_cost = calculate_tour_cost(new_tour)
        if new_cost < current_cost or math.exp((current_cost - new_cost) / temp) > random.random():
            tour, current_cost = new_tour, new_cost
        
        temp *= 1 - cooling_rate
    
    return tour, current_cost

# Constructing Initial Tours
initial_tours = create_initial_solution()

# Optimization Loop
optimized_tours = []
costs = []
for tour in initial_tours:
    optimized_tour, cost = simulated_annealing(tour)
    optimized_tours.append(optimized_tour)
    costs.append(cost)

# Aggregate total cost
total_cost = sum(costs)

# Output results
for idx, (tour, cost) in enumerate(zip(optimized_tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")