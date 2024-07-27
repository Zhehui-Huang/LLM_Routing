import math
import random

# Define the cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Parameters
num_robots = 8
starting_city = 0  # All robots start from city 0

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize the tours for each robot
tours = [[] for _ in range(num_robots)]
for i in range(len(cities)):
    tours[i % num_robots].append(i)

# Function to calculate the total cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

# Simulated Annealing parameters
T = 1000  # Initial temperature
T_min = 1  # Minimum temperature
alpha = 0.99  # Cooling rate
def simulated_annealing(tour):
    current_tour = tour[:]
    current_cost = calculate_tour_cost(current_tour)
    while T > T_min:
        for _ in range(100):  # Iterations at each temperature level
            i, j = random.randint(1, len(tour) - 1), random.randint(1, len(tour) - 1)
            new_tour = current_tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / T):
                current_tour, current_cost = new_tour, new_cost
        global T
        T *= alpha
    return current_tour


# Optimize each tour using Simulated Annealing
optimized_tours = [simulated_annealing(tour) for tour in tours]

# Output the tours and their costs
overall_total_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {[starting_city] + tour + [starting_city]}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}\n")

print(f"Overall Total Travel Cost: {overall_total_cost}")