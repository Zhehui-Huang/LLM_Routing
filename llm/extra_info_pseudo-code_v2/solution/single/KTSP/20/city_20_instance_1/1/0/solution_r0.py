import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute the total tour distance
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initial simple tour generator
def generate_initial_solution(k, available_cities):
    solution = [0]
    while len(solution) < k:
        new_city = random.choice(list(set(available_cities) - set(solution)))
        solution.append(new_city)
    solution.append(0)  # Return to depot
    return solution

# Finding the best solution by permutations
def find_best_tour(k):
    available_cities = list(cities.keys())
    best_tour = None
    min_cost = float('inf')
    
    # Check each permutation of k-2 cities (excluding depot)
    for perm in permutations(available_cities[1:], k - 2):
        tour = [0] + list(perm) + [0]
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Find the best tour for k = 7
tour, cost = find_best_tour(7)
print("Tour:", tour)
print("Total travel cost:", cost)