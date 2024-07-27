import random
import math
from itertools import permutations

# Coordinates of cities
cities_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities without following_dict[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    """Generate an initial solution."""
    cities = list(range(1, 15))
    random.shuffle(cities)
    return [0] + cities[:7] + [0]

def shake(s, n):
    """Shake the current solution within n-th neighborhood."""
    s_prime = s[1:-1]  # exclude the depot
    random.shuffle(s_prime)
    return [0] + s_prime + [0]

def local_search(s):
    """Local search improvement using swapping neighborhoods."""
    n = len(s)
    best_distance = total_distance(s)
    best_s = list(s)
    improved = True
    while improved:
        improved = False
        for i in range(1, n-2):
            for j in range(i + 1, n-1):
                new_tour = list(s)
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # swap two cities
                new_distance = total_distance(new_tour)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_s = new_tour
                    improved = True
    return best_s

def gvns(k_max, itermax):
    s = generate_initial_solution()
    best_s = s
    best_cost = total_distance(s)
    
    for _ in range(itermax):
        for k in range(1, k_max + 1):
            s_prime = shake(s, k)
            s_prime_prime = local_search(s_prime)
            cost = total_distance(s_prime_prime)
            if cost < best_cost:
                best_s = s_prime_prime
                best_cost = cost
                break
    
    return best_s, best_cost


# Parameters
k_max = 3
itermax = 100

# Run GVNS
solution, cost = gvns(k_max, itermax)

# Output results
print("Tour:", solution)
print("Total travel cost:", cost)