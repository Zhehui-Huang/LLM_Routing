import math
import random

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
    all_cities = list(range(1, len(cities)))  # Exclude the depot city
    random.shuffle(all_cities)  # Randomize city order for initial tour distribution
    parts = [all_cities[i::num_robots] for i in range(num_robots)]  # Split cities among robots
    tours = [[0] + part + [0] for part in parts]  # Start and end each tour at the depot
    return tours

# Calculate the total travel cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Local search - try to find a better configuration in the neighborhood
def local_search(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    for i in range(1, len(tour)-2):
        for j in range(i+1, len(tour)-1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
    return best_tour

# Variable Neighborhood Search
def variable_neighborhood_search(tours):
    best_solution = [local_search(tour) for tour in tours]
    best_max_cost = max(tour_cost(tour) for tour in best_solution)
    
    improved = True
    while improved:
        improved = False
        for _ in range(10):  # Number of shaking operations
            # Shaking - randomly swap cities between tours
            r1, r2 = random.sample(range(len(tours)), 2)
            if len(tours[r1]) > 2 and len(tours[r2]) > 2:
                i1, i2 = random.randint(1, len(tours[r1])-2), random.randint(1, len(tours[r2])-2)
                tours[r1][i1], tours[r2][i2] = tours[r2][i2], tours[r1][i1]
                new_cost = max(tour_cost(tour) for tour in tours)
                if new_cost < best_max_cost:
                    best_solution = [local_search(tour) for tour in tours]
                    best_max_cost = new_cost
                    improved = True
    return best_solution

# Initial tour setup and optimization
initial_tours = initial_solution()
optimized_tours = variable_neighborhood_search(initial_tours)

# Output the resulting tours and compute the max travel cost
max_cost = 0
for i, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    max_cost = max(max_cost, cost)
print(f"Maximum Travel Cost: {max_cost}")