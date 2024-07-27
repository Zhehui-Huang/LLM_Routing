import itertools
import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_travel_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour)-1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def generate_initial_solution(depot, cities, k):
    sampled_cities = random.sample(cities, k-1)
    tour = [depot] + sampled_cities + [depot]
    return tour

def optimize_tour(tour, coordinates):
    best_tour = tour[:]
    best_cost = total_travel_cost(tour, coordinates)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if j - i == 1:
                    continue  # adjacent cities - swap doesn't make sense here
                new_tour = tour[:]
                new_tour[i:j] = tour[i:j][::-1]  # this reverses the segment between i and j
                new_cost = total_travel_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
    return best_tour, best_cost

def solve_k_tsp(coordinates, k, trials=10000):
    cities = list(range(1, len(coordinates)))  # excludes depot (0) which is implicit
    depot = 0
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(trials):
        current_tour = generate_initial_solution(depot, cities, k)
        current_tour, current_cost = optimize_tour(current_tour, coordinates)
        
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
    
    return best_tour, best_cost

coordinates = [
    (54, 87), # City 0
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# We have set the number of cities k including the depot to be 8
tour, cost = solve_k_tsp(coordinates, 8)

print("Tour:", tour)
print("Total travel cost:", round(cost, 2))