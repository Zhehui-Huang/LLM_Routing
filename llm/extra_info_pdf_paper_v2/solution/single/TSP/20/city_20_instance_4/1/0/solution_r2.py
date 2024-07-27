import math
import random

# Coordinates of cities, including the depot at index 0
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between two cities
def distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate a random initial tour
def initial_tour():
    tour = list(range(1, len(cities)))  # Start from 1 to exclude the depot
    random.shuffle(tour)
    tour = [0] + tour + [0]  # Start and end at the depot city
    return tour

# 2-opt algorithm to optimize the tour
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:  # Skip adjacent edges
                    continue
                current_distance = distance(tour[i], tour[i-1]) + distance(tour[j], tour[j+1])
                new_distance = distance(tour[i], tour[j]) + distance(tour[i-1], tour[j+1])
                if new_distance < current_distance:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improvement = True
    return tour

# Compute the total cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Optimized function to find the best tour
def optimize_tour():
    best_tour = initial_tour()
    best_tour = two_opt(best_tour)
    best_cost = calculate_total_cost(best_tour)
    return best_tour, best_cost

# Find the TSP solution with a 2-opt approach
final_tour, final_cost = optimize_tour()
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))