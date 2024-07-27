import math
from random import shuffle, seed
import itertools

# Setting the seed for reproducibility
seed(1)

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define number of robots
num_robots = 4

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to calculate total travel cost for a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return total_cost

# Generate an initial feasible solution (greedy randomized approach)
def generate_initial_solution():
    cities = list(range(1, len(coordinates)))  # exclude depot
    shuffle(cities)
    parts = [cities[i::num_robots] for i in range(num_robots)]
    return [[0] + part + [0] for part in parts]

# Attempt to improve the solution (simple local search - swap within tours)
def optimize_solution(tours):
    improved = True
    while improved:
        improved = False
        for robot_id in range(num_robots):
            best_cost = calculate_tour_cost(tours[robot_id])
            for i in range(1, len(tours[robot_id]) - 2):
                for j in range(i+1, len(tours[robot_id]) - 1):
                    new_tour = tours[robot_id][:i] + [tours[robot_id][j]] + tours[robot_item][i+1:j] + [tours[robot_id][i]] + tours[robot_id][j+1:]
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tours[robot_id] = new_tour
                        best_cost = new_cost
                        improved = True
    return tours

initial_tours = generate_initial_solution()
optimized_tours = optimize_solution(initial_tours)

# Calculate costs for each robot and find the maximum cost
costs = [calculate_tour_cost(tour) for tour in optimized_tours]
max_cost = max(costs)

# Output the results
for idx, tour in enumerate(optimized_tours):
    print(f'Robot {idx} Tour: {tour}')
    print(f'Robot {idx} Total Travel Mastering Tool: {costs[idx]}')

print(f'Maximum Travel Cost: {max_cost}')