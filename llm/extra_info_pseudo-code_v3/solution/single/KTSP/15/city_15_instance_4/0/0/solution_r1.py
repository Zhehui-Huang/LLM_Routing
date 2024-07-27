import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate the initial random solution
def generate_initial_solution():
    available_cities = list(cities.keys())
    available_cities.remove(0)
    selected_cities = random.sample(available_cities, 11)
    tour = [0] + selected_cities + [0]
    return tour

# Calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i+1])
    return cost

# Perform local search by swapping two cities in the tour
def local_search(tour):
    best_cost = calculate_tour_cost(tour)
    best_tour = tour[:]
    
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap cities
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
                
    return best_tour

# Shaking: simply use permutation in the city list by excluding the first and the last depot city
def shake(tour):
    core_tour = tour[1:-1]
    random.shuffle(core_tour)
    return [tour[0]] + core_tour + [tour[-1]]

# GVNS
def gvns(max_iterations=100):
    best_tour = generate_initial_solution()
    best_cost = calculate_tour_cost(best_tour)
    
    for _ in range(max_iterations):
        new_tour = shake(best_tour)
        improved_tour = local_search(new_tour)
        improved_cost = calculate_tour_cost(improved_tour)
        
        if improved_cost < best_cost:
            best_tour = improved_tour[:]
            best_cost = improved_cost
    
    return best_tour, best_cost

# Execute the algorithm
best_tour_found, best_tour_cost = gvns()

print("Tour:", best_tour_found)
print("Total travel cost:", round(best_tour_cost, 2))