import random
import math
from itertools import permutations

# Distances and city coordinates are computed as follows:
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Cost function
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_solution(k, total_cities):
    tour = [0]  # Start at the depot
    while len(tour) < k:
        new_city = random.choice([x for x in range(total_cities) if x not in tour])
        best_position = -1
        best_cost = float('inf')
        for i in range(1, len(tour) + 1):
            new_tour = tour[:i] + [new_city] + tour[i:]
            cost = calculate_tour_cost(new_tour + [0])  # Complete the tour to calculate cost
            if cost < best_cost:
                best_cost = cost
                best_position = i
        tour.insert(best_position, new_city)
    tour.append(0)  # End at the depot
    return tour

def shake(tour):
    a, b = sorted(random.sample(range(1, len(tour) - 2), 2))
    tour = tour[:a] + tour[a:b][::-1] + tour[b:]
    return tour

def local_search(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improvement = True
    return tour

def vnd(tour):
    return local_search(tour)

def gvns(k, total_cities, itermax):
    best_tour = generate_initial_solution(k, total_cities)
    best_cost = calculate_tour_cost(best_tour)
    iter = 0
    while iter < itermax:
        new_tour = shake(best_tour[:])
        new_tour = vnd(new_tour)
        new_cost = calculate_tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
        iter += 1
    return best_tour, best_cost

# Running GVNS for k-TSP with 12 cities (including the depot city)
k = 13  # includes the depot as last city again for completion
itermax = 100 
best_tour, best_cost = gvns(k, len(cities), itermax)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)