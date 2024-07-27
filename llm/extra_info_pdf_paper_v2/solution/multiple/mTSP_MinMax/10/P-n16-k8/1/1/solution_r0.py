import math
import random
from itertools import permutations

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots available
num_robots = 8

# Initialize robots' tours
def initial_solution():
    # Excluding the depot city from routing
    all_cities = list(range(1, len(cities)))
    random.shuffle(all_cities)
    parts = [all_cities[i::num_robots] for i in range(num_robots)]
    tours = [[0] + part + [0] for part in parts]  # Each tour starts and ends at the depot
    return tours

# Calculate tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Variable Neighborhood Search
def variable_neighborhood_search(tours):
    best_solution = tours
    best_max_cost = max(tour_cost(tour) for tour in tours)
    
    for k in range(1, 10):  # 10 levels of neighborhoods
        new_solution = shake(tours, k)
        new_max_cost = max(tour_cost(tour) for tour in new_solution)
        if new_max+cost < best_max_cost:
            best_solution = new_solution
            best_max_cost = new_max_cost
    return best_solution

# Shake function to generate new neighborhoods
def shake(tours, k):
    # Swap random cities between tours. 'k' defines number of swaps
    for _ in range(k):
        r1, r2 = random.sample(range(len(tours)), 2)
        if len(tours[r1]) > 2 and len(tours[r2]) > 2:
            c1, c2 = random.choice(tours[r1][1:-1]), random.choice(tours[r2][1:-1])
            idx1, idx2 = tours[r1].index(c1), tours[r2].index(c2)
            tours[r1][idx1], tours[r2][idx2] = tours[r2][idx2], tours[r1][idx1]
    return tours

# Find a good initial solution and improve it
initial_tours = initial_solution()
optimized_tours = variable_neighborhood_search(initial_tours)

# Output the tours and costs
max_cost = 0
for i, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    max_cost = max(max_cost, cost)
print(f"Maximum Travel The travel cost: {max_cost}")