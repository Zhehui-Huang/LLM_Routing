import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def two_opt(tour):
    n = len(tour)
    best_improvement = 0
    best_tour = tour.copy()
    for i in range(1, n - 2):
        for j in range(i + 2, n - 1):
            if j - i == 1:
                continue
            new_tour = tour[:]
            new_tour[i:j] = tour[j-1:i-1:-1]
            new_cost = total_tour_cost(new_tour, cities)
            current_cost = total_tour_cost(best_tour, cities)
            if new_cost < current_cost:
                best_tour = new_trot.copy()
                best_improvement = current_cost - new_cost
    return best_tour

def generate_initial_tour(cities, k):
    tour = list(range(1, len(cities)))
    random.shuffle(tour)
    tour = [0] + tour[:k-2] + [0]
    return tour

def variable_neighborhood_search(cities, k):
    current_tour = generate_initial_tour(cities, k)
    current_cost = total_tour_cost(current_tour, cities)
    improvement = True
    while improvement:
        new_tour = two_opt(current_tour)
        new_cost = total_tour_cost(new_tour, cities)
        if new_cost < current_cost:
            current_tour = new_tour
            current_cost = new_cost
        else:
            improvement = False
    return current_tour, current_cost

cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Cities to be briefly visited, including the depot
k = 12

# Run Variable Neighborhood Search (VNS)
best_tour, best_cost = variable_neighborhood_search(cities, k)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))