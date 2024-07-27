import random
import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Setting parameters
num_robots = 8
max_iterations = 1000
max_consecutive_nonimproving = 50
tabu_tenure = 20  # Number of iterations move is considered tabu

# Initialize tours
tours = {robot: [0] for robot in range(num_robots)}
unvisited_cities = set(cities.keys()) - {0}

# Nearest Neighbor initial solution
for robot in tours:
    current_city = 0
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tours[robot].append(nearest_city)
        current_city = nearest_city
        unvisited_cities.remove(nearest_city)
        if len(tours[robot]) >= len(cities) / num_robots:
            break

# Tabu list
tabu_list = {}

def calculate_total_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Try to optimize the tours
iteration = 0
best_tours = tours.copy()
best_cost = sum(calculate_total_cost(tour) for tour in best_tours.values())

while iteration < max_iterations:
    for robot, tour in tours.items():
        original_cost = calculate_total_cost(tour)
        # Try all possible swaps
        for i, j in combinations(range(1, len(tour)), 2):
            tour[i], tour[j] = tour[j], tour[i]
            new_cost = calculate_total_cost(tour)
            if (tour, (i, j)) not in tabu_list and new_cost < original_cost:
                tabu_list[(tuple(tour), (i, j))] = tabu_tenure
            else:
                tour[i], tour[j] = tour[j], tour[i]  # Swap back

    # Reduce tabu tenure
    tabu_list = {(move, indices): tenure - 1 for (move, indices), tenure in tabu_list.items() if tenure > 1}

    current_cost = sum(calculate_total_cost(tour) for tour in tours.values())
    if current_cost < best_cost:
        best_cost = current_cost
        best_tours = tours.copy()

    iteration += 1

# Output result
overall_total_cost = 0

for robot, tour in best_tours.items():
    tour_cost = calculate_total_cost(tour)
    overall_total_cost += tour.__add__(tour_cost)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")