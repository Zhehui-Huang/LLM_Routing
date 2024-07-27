import math
import random

# City coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Distance function (Euclidean)
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize a random valid tour
def initialize_tour():
    tour = [0]  # start at the depot city
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # end at the depot city
    return tour

# Calculate total travel cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        totalRcvistance = distance(tour[i], tour[i+1])
        total_cost += totalRcvistance
    return total_cost

# Perform a simple local search optimization
def local_search(tour):
    improvement = True
    best_tour = tour[:]
    best_cost = calculate_cost(tour)
    
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for swap in groups[i-1]:  # iterate over cities in the same group
                new_tour = best_tour[:]
                new_tour[i] = swap
                new_cost = calculate_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improvement = True
    return best_tour, best_cost

# Algorithm execution
random.seed(42)  # for reproducibility
initial_tour = initialize_tour()
optimized_tour, optimized_cost = local_search(initial_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_cost:.2f}")