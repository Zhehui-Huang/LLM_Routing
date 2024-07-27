import random
import math
from itertools import permutations

# Cities coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initializing solution
num_robots = 4
tour = {}
for i in range(num_robots):
    tour[i] = [0]  # All robots start at city 0

# Assign cities equally approx among robots. Here we do simple even distribution. More sophisticated partitioning can be done.
remaining_cities = list(range(1, 22))
random.shuffle(remaining_cities)
split_cities = [remaining_cities[i::num_robots] for i in range(num_robots)]

# Function to calculate tour cost
def calculate_tour_cost(t):
    cost = 0
    for j in range(len(t)-1):
        cost += euclidean_distance(cities[t[j]], cities[t[j+1]])
    return cost

# Distribute the cities to robots and calculate a basic greedy tour
for i in range(num_robots):
    tour[i].extend(split_cities[i])

# Tabu search parameters
max_iterations = 1000
tabu_list = []
tabu_list_size = 50

# Start the Tabu Search
for it in range(max_iterations):
    # Making the neighborhood
    for i in range(num_robots):
        if len(tour[i]) > 2:
            # Swap two cities on the tour
            a, b = random.sample(range(1, len(tour[i])), 2)
            tour[i][a], tour[i][b] = tour[i][b], tour[i][a]
    
    # Checking in tabu list
    if tour in tabu_list:
        continue
    
    # Calculate the cost
    new_cost = sum([calculate_tour_cost(tour[i]) for i in range(num_robots)])
    if 'best_cost' not in locals() or new_cost < best_cost:
        best_cost = new_cost
        best_tour = tour.copy()
    
    # Update tabu list
    tabu_list.append(tour.copy())
    if len(tabu_list) > tabu_list_size:
        tabu={c}.list.pop(0)

# Final calculations and output
total_cost = 0
for i in range(num_robots):
    tour_cost = calculate_tour_cost(best_tour[i])
    total_cost += tour_cost
    print(f"Robot {i} Tour: {best_tour[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")