import random
import math
from itertools import combinations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate initial solution (greedy algorithm, selecting random cities)
def initial_solution(total_cities, num_cities):
    selected = set([0])
    while len(selected) < num_cities:
        selected.add(random.randint(1, total_cities - 1))
    return list(selected) + [0]

# Local search strategy: Two Opt (swap two cities to find a better tour)
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1] # this is the 2-opt swap
                if total_distance(new_tour) < total_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Implementing a simple variant of GVNS
def gvns(kmax, num_cities):
    best = initial_solution(20, num_cities)
    k = 1
    while k <= kmax:
        new_solution = two_opt(best)
        if total_distance(new_solution) < total_distance(best):
            best = new_solution
            k = 1
        else:
            k += 1
    return best

# Find a tour using the GVNS approach
num_cities = 16  # including the depot city
kmax = 10  # depth of search
tour = gvns(kmax, num_cities)
final_tour = two_opt(tour)  # Final optimization using 2-opt
final_cost = total_distance(final_tour)

# Output
print("Tour:", final_tour)
print("Total travel cost:", final_cost)