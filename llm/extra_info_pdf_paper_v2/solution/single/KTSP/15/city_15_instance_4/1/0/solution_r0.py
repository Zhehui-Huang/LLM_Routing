import math
import random
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_pass(tour[i], tour[i+1])
    return total_cost

def euclidean_pass(c1, c2):
    return euclidean_distance(cities[c1], cities[c2])

def initial_solution(cities, k):
    return random.sample(range(1, len(cities)), k-1) + [0]

def local_search(tour):
    best_cost = total_tour_cost(tour, cities)
    best_tour = tour[:]
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)):
                if j-i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                new_cost = total_tour_cost(new_tour, cities)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    made_improvement = True
        tour = best_tour
    return best_tour

def variable_neighborhood_search(cities, k, max_attempts=1000):
    best_solution = initial_solution(cities, k)
    best_solution.append(0)  # Return to depot
    best_solution.insert(0, 0)  # Start at depot
    best_cost = total_tour_cost(best_solution, cities)

    attempts = 0
    while attempts < max_attempts:
        new_solution = local_search(best_solution)
        new_cost = total_tour_cost(new_solution, cities)
        if new_cost < best_cost:
            best_cost = new_cost
            best_solution = new_solution
            attempts = 0
        else:
            attempts += 1

    return best_solution, best_cost

# Define city coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Execute the variable neighborhood search
tour, cost = variable_neighborhood_search(cities, 12)
print("Tour:", tour)
print("Total travel cost:", cost)