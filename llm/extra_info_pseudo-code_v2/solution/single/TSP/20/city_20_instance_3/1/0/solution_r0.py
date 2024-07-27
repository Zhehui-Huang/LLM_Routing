import math
import random
from itertools import permutations

# Define the coordinates of the depot and cities
cities = [
    (30, 56),  # Depot city 0
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate an initial tour randomly
def initial_tour(num_cities):
    tour = list(range(1, num_cities))  # start from city 1 to city n-1
    random.shuffle(tour)
    return [0] + tour + [0]  # add the depot (start/end)

# Calculate the total travel cost of the tour
def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i+1])
    return total_dist

# Randomized tour for starting Lin-Kernighan
initial = initial_tour(len(cities))
current_dist = calculate_total_distance(initial)

# Simulated Annealing Parameters
temperature = 10000
cooling_rate = 0.995
min_temperature = 1

def simulated_annealing(tour, current_dist):
    t = temperature
    best_tour = tour[:]
    best_dist = current_dist

    while t > min_temperature:
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]  # Reverse the segment
        new_dist = calculate_total_distance(new_tour)

        if new_dist < current_dist or random.random() < math.exp((current_dist - new_dist) / t):
            tour, current_dist = new_tour, new_dist

            if new_dist < best_dist:
                best_dist, best_tour = new_dist, new_tour[:]
                
        t *= cooling_rate

    return best_tour, best_dist

final_tour, final_dist = simulated_annealing(initial, current_dist)

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", round(final_dist, 2))

# Note: The provided solution focuses on reasonable time-constrained approximations suitable for
# real-world applications given the computation limits and large input size.