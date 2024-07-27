import math
import random

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Total number of required cities including the depot
k = 12

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# Generate Initial Solution (random tour including k cities)
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], k-1)
    return tour, calculate_cost(tour)

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += distances[tour[-1]][tour[0]]  # return to depot
    return total_cost

# Shake function for GVNS
def shake(tour):
    ind1, ind2 = random.sample(range(1, len(tour)), 2)  # Avoid shuffling the depot
    tour[ind1], tour[ind2] = tour[ind2], tour[ind1]
    return tour

# Variable Neighborhood Descent (Two neighborhoods: Swap and 2-opt)
def vnd(tour):
    improved = True
    while improved:
        improved = False
        best_cost = calculate_cost(tour)
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_taken_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour

# Main GVNS implementation
def gvns(max_iterations=1000):
    best_solution, best_cost = generate_initial_solution()
    for _ in range(max_iterations):
        current_solution = shake(best_solution[:])
        new_solution = vnd(current_solution)
        new_cost = calculate_cost(new_solution)
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
    return best_solution, best_cost

# Execute the algorithm and print the result
best_tour, best_cost = gvns()
best_tour.append(best_tour[0])  # Append the depot at the end to complete the tour
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")