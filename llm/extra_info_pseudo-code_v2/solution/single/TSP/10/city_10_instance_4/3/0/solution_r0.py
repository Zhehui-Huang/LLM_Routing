import math
import random

# Define the coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(tour[i-1], tour[i])
    return total_cost

def two_opt_swap(tour):
    best_tour = tour[:]
    best_distance = total_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j+1] = tour[i:j+1][::-1]
                new_distance = total_tour_cost(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        tour = best_tour[:]
    return best_tour, best_distance

# Create an initial feasible tour
initial_tour = list(cities.keys())
random.shuffle(initial_tour[1:]) # Shuffle only cities but start with depot city 0
initial_tour.append(0) # Complete the tour by returning to the depot

# Improve the initial tour using 2-opt
optimized_tour, optimized_distance = two_opt_swap(initial_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {optimized_distance:.2f}")