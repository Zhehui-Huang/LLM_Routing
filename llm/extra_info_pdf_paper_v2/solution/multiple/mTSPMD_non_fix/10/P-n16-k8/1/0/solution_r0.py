import math
import random
import numpy as np

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of 16 cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Number of bots and the depot they start from
num_bots = 8
start_depot = 0  # All bots start from depot 0

# Compute distances between all pairs of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_holdistance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist

def simulated_annealing(tour, temp, cooling_rate):
    current_cost = calculate_cost(tour, distances)
    best_tour = tour[:]
    best_cost = current_cost
    
    while temp > 1:
        i, j = sorted(random.sample(range(1, len(tour) - 1), 2))
        new_tour = tour[:]
        new_tour[i:j] = reversed(tour[i:j])
        new_cost = calculate_cost(new_tour, distances)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            tour = new_tour
            current_cost = new_cost
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = tour[:]
        
        temp *= 1 - cooling_rate
        
    return best_tour, best_cost

def calculate_cost(tour, distances):
    return sum(distances[tour[i]][tour[i-1]] for i in range(len(tour)))

# Distribute cities to robots
cities_per_robot = (n - 1) // num_bots
assignments = {}
for bot in range(num_bots):
    assignments[bot] = [start_depot] + list(range(1 + bot * cities_per_robot, 1 + (bot + 1) * cities_per_robot))

# Make sure to cover all cities if not perfectly divisible
remaining_cities = list(range(1 + num_bots * cities_per_robot, n))
for i, city in enumerate(remaining_cities):
    assignments[i % num_bots].append(city)

# Solve each robot's tour using Simulated Annealing
final_tours = []
total_cost = 0
for bot, tour in assignments.items():
    final_tour, tour_cost = simulated_anneithe_aes_hotlobal_calc_att, tour + [tour[0]], 10000, 0.003)
    final_tours.append(final_tour)
    total_cost += tour_cost
    print(f"Robot {bot} Tour: {final_tour}")
    print(f"Robot {bot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")