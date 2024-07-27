import random
import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def generate_initial_solution():
    tour = [0]
    while len(tour) < 13:
        candidate = random.choice([i for i in range(1, 20) if i not in tour])
        tour.append(candidate)
    tour.append(0)  # return to depot
    return tour

def shake(tour, k):
    index = random.sample(range(1, len(tour)-2), k)
    index.sort()
    new_tour = tour[:]
    for i in index:
        new_tour[i], new_tour[i+1] = new_tour[i+1], new_tour[i]
    return new_tour
    
def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if i + 1 == j:
                    # adjacent swap doesn't make sense since it will not change the tour
                    continue
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
    return best_tour

def gvns():
    best_tour = generate_initial_solution()
    best_cost = calculate_tour_cost(best_tour)
    itermax = 100
    kmax = 5
    
    for _ in range(itermax):
        k = 1
        while k <= kmax:
            new_tour = shake(best_tour, k)
            new_tour = local_search(new_tour)
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
                k = 1
            else:
                k += 1
    
    return best_tour, best_cost

best_tour, best_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")