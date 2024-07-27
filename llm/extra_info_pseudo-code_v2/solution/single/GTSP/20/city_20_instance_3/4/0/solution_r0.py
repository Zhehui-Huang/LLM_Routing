import random
import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups
city_groups = [
    [4, 10, 13, 17],    # Group 0
    [6, 7, 14],         # Group 1
    [9, 12, 16],        # Group 2
    [2, 5, 15],         # Group 3
    [1, 3, 19],         # Group 4
    [8, 11, 18]         # Group 5
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_tour():
    tour = [0]  # start at the depot
    selected_cities = []
    for group in city_groups:
        selected_city = random.choice(group)
        selected_cities.append(selected_city)
    tour.extend(selected_cities)
    tour.append(0)  # return to depot
    return tour

def local_search(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:  # Don't move the depot
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# Generating an initial tour and performing optimization
initial_tour = generate_initial_tour()
optimized_tour = local_search(initial_tour)

# Calculating the cost of the optimized tour
tour_cost = calculate_tour_cost(optimized_tour)

# Output required format
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {tour_cost}")