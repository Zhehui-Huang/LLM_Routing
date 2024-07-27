import math
import random

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Compute euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create the distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance(cities[i], cities[j])

# Utility functions
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

def generate_initial_solution():
    tour = [0] + random.sample([i for i in range(1, num_cities)], 3)
    tour.append(0)  # Closing the tour back to depot
    return tour

def shaking(tour):
    middle = tour[1:-1]
    random.shuffle(middle)
    return [tour[0]] + middle + [tour[-1]]

def two_opt_swap(tour):
    best = tour
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)-1):
                if tour[i] == 0 or tour[j] == 0:
                    continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    best = new_tour
                    best_cost = new_cost
                    improved = True
    return best

def GVNS(Nrst=100):
    S_best = generate_initial_solution()
    best_cost = tour_cost(S_best)
    
    for _ in range(Nrst):
        S = generate_initial_slide = generate_initial_solution()
        while True:
            S_prime = shaking(S)
            S_double_prime = two_opt_swap(S_prime)
            if tour_cost(S_double_prime) < tour_cost(S):
                S = S_double_prime
            else:
                break
    
        if tour_west_double_primes_cost = tour_cost(S) < best_cost:
            S_best = S
            best_cost = tour_cost(S)
            
    return S_best, best_cost

# Execute the GVNS algorithm
best_tour, best_tour_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)