import math
import random

# Define cities coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Distance calculation using Euclidean distance
def calculate_distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate all distances and store in a matrix
n = len(cities)
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Initial tour generation with k=8 including depot city 0
def initial_tour():
    tour = [0] + random.sample(list(cities.keys())[1:], 7)
    tour.append(0)  # Return to the depot
    return tour

# Calculate total travel cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Swap neighborhood: swaps two cities in the tour
def create_neighborhood(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    for i in range(1, len(tour) - 2):  # skip depot city for swapping
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    return best_tour

# Implement GVNS
def variable_neighborhood_search(max_iterations=500):
    tour = initial_tour()
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    iteration = 0
    while iteration < max_iterations:
        new_tour = create_neighborhood(best_tour)
        new_cost = tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour[:], new_cost
        iteration += 1
    return best_tour, best_cost

# Perform the search
tour_result, cost_result = variable_neighborhood_search()
print("Tour:", tour_result)
print("Total travel cost:", cost_result)