import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def two_opt(tour, cities):
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]
                if total_tour_cost(new_tour, cities) < total_tour_cost(best_tour, cities):
                    best_tour = new_tour[:]
                    improved = True
        tour = best_tour[:]
    return best_tour

def generate_initial_tour(cities, k):
    tour = random.sample(range(1, len(cities)), k-2)
    tour = [0] + tour + [0]
    return tour

def variable_neighborhood_search(cities, k):
    current_tour = generate_initial_tour(cities, k)
    current_cost = total_tour_cost(current_tour, cities)
    for _ in range(100):  # Arbitrary number of iterations for potential improvement
        new_tour = two_opt(current_tour, cities)
        new_cost = total_tour_cost(new_tour, cities)
        if new_cost < current_cost:
            current_tour = new_tour
            current_cost = new_cost
    return current_tour, current_cost

cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Cities to be visited, including the depot
k = 12

# Run the Variable Neighborhood Search (VNS) algorithm
best_tour, best_cost = variable_neighborhood_search(cities, k)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))