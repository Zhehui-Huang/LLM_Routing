import math
import random

# Coordinates of the cities, depot city being the index 0
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def max_distance(tour):
    return max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Initialize a random tour
def initial_tour():
    tour = list(range(1, len(cities)))
    random.shuffle(tour)
    return [0] + tour + [0]

# Generate a neighboring solution by swapping two cities
def get_neighbor(tour):
    a, b = random.sample(range(1, len(cities)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

# Simulated Annealing algorithm
def simulated_annealing():
    current_tour = initial_tour()
    current_temp = 1000
    cooling_rate = 0.995
    min_temp = 1
    while current_temp > min_temp:
        next_tour = get_neighbor(current_tour[:])
        current_cost = max_distance(current_tour)
        next_cost = max_distance(next_tour)
        if next_cost < current_cost or random.uniform(0,1) < math.exp((current_cost - next_cost) / current_temp):
            current_tonur = next_tour
        current_temp *= cooling_rate
    return current_tour

# Run simulated annealing
optimal_tour = simulated_annealing()

# Calculate distances
total_cost = total_distance(optimal_tour)
max_dist = max_distance(optimal_tour)

print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)