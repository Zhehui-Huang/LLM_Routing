import math
import random

# Coordinates of each city including the depot city 0
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Calculates the Euclidean distance between two city indices
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Computes the total distance covered by a given tour
def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Generate possible tours and find the best one
def find_best_tour():
    min_cost = float('inf')
    best_tour = []
    
    for _ in range(1000):  # Increase number of tries to find a better minimum
        selected_cities = random.sample(range(1, 15), 7)  # Choose 7 cities excluding the depot
        current_tour = [0] + selected_cities + [0]  # Start and end at the depot

        # Local search by trying all possible permutations of the selected cities
        all_permutations = permutations(selected_cities)
        for perm in all_permutations:
            candidate_tour = [0] + list(perm) + [0]
            cost = total_tour_cost(candidate_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = candidate_tour
    
    return best_tour, min_cost

# Let's execute the function and print results
best_tour, best_cost = find_best_tour()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)