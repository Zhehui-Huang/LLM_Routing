import math
import random

# City coordinates indexed from 0 to 9
cities = [
    (84, 67),  # Depot city
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generates a random tour starting and ending at the depot
def initial_tour():
    tour = list(range(1, len(cities)))  # start from 1 to omit the depot initially
    random.shuffle(tour)
    return [0] + tour + [0]  # adding depot as start and end

# Function to compute the total distance of the tour
def tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

# Heuristic improvement: 2-opt Swap
def two_opt(tour):
    best_distance = tour_distance(tour)
    best_tour = tour
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue  # consecutively linked cities - no change
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = tour_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
        tour = best_tour
    return best_tour, best_distance

# Create an initial tour and improve it
random.seed(42)
initial_t = initial_tour()
opt_tour, opt_distance = two_opt(initial_t)

# Output the result
print("Tour:", opt_tour)
print("Total travel cost:", round(opt_distance, 2))