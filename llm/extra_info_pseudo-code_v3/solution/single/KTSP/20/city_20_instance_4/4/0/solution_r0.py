import random
import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 15)
    tour.append(0)  # Return to the depot
    return tour

# Calculate total travel cost
def total_travel_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shake function: Swap two cities in the tour
def shake(tour):
    new_tour = tour[1:-1]  # Exclude the depot city from swaps
    i1, i2 = random.sample(range(len(new_tour)), 2)
    new_tour[i1], new_tour[i2] = new_tour[i2], new_tour[i1]
    return [0] + new_tour + [0]

# Variable Neighborhood Descent
def vnd(tour):
    improved = True
    while improved:
        improved = False
        for i1 in range(1, len(tour)-2):
            for i2 in range(i1+1, len(tour)-1):
                if i1 != i2:
                    new_tour = tour[:]
                    new_tour[i1], new_tour[i2] = new_tour[i2], new_tour[i1]
                    if total_travel_cost(new_tour) < total_travel_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# GVNS
def gvns(max_iterations=100):
    best_tour = generate_initial_solution()
    best_cost = total_travel_cost(best_tour)

    for _ in range(max_iterations):
        current_tour = shake(best_tour)
        improved_tour = vnd(current_tour)
        improved_cost = total_travel_cost(improved_tour)
        
        if improved_cost < best_cost:
            best_tour = improved_tour
            best_cost = improved_cost

    return best_tour, best_cost

# Find the solution
best_tour, best_cost = gvns()

# Print the output
print("Tour:", best_tour)
print("Total travel cost:", best_cost)