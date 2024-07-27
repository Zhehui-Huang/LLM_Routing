import math
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Initial tours for two robots starting from depot 0
robots = {0: [0], 1: [0]}

# Function to calculate Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Initial distribution of cities to robots
unvisited = list(cities.keys())[2:]  # Cities except depots
random.shuffle(unvisited)  # Shuffle to create an initial random path
mid = len(unvisited) // 2
robots[0].extend(unvisited[:mid])
robots[1].extend(unvisited[mid:])

# Simulated Annealing Function
def simulated_annealing(tour):
    temp = 10000
    cooling_rate = 0.995
    while temp > 1:
        # Implement a single swap
        i, j = random.sample(range(1, len(tour)), 2)
        new_tour = tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        # Calculate the cost difference
        current_cost = sum(distance(tour[k], tour[k + 1]) for k in range(len(tour) - 1))
        new_cost = sum(distance(new_tour[k], new_tour[k + 1]) for k in range(len(new_tour) - 1))
        
        # Acceptance probability
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            tour[:] = new_tour
        
        temp *= cooling_rate

# Apply Simulated Annealing to each robot tour
for key in robots:
    robots[key].append(0)  # To complete the loop for calculating initial cost easily
    simulated_annealing(robots[key])

# Output
overall_cost = 0
for key in robots:
    tour_cost = sum(distance(robots[key][i], robots[key][i+1]) for i in range(len(robots[key]) - 1))
    overall_cost += tour_cost
    print(f"Robot {key} Tour: {robots[key]}")
    print(f"Robot {key} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")