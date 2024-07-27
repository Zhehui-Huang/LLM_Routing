import math
from random import shuffle, randint, seed
import copy

# Fixed seed for reproducibility
seed(1)

# Position of cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_and_max_distance(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    # Closing the loop
    closing_distance = calculate_euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_distance += closing_distance
    max_distance = max(max_distance, closing_distance)
    return total_distance, max_distance

def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def iterative_local_search(cities, iterations=1000):
    best_tour = list(range(len(cities)))
    shuffle(best_tour)
    best_total, best_max = calculate_total_and_max_distance(best_tour, cities)
    
    for _ in range(iterations):
        perturbed_tour = copy.deepcopy(best_tour)
        # Perturbation: double-bridge move
        a, b, c, d = sorted(randint(1, len(cities) - 2) for _ in range(4))
        perturbed_tour = perturbed_tour[:a] + perturbed_tour[c:d+1][::-1] + perturbed_tour[b:c+1][::-1]+ perturbed_tour[a:b+1][::-1] + perturbed_tour[d+1:]
        perturbed_total, perturbed_max = calculate_total_and_max_distance(perturbed_tour, cities)
        
        for i in range(1, len(cities) - 1):
            for k in range(i + 1, len(cities)):
                new_tour = two_opt_swap(perturbed_tour, i, k)
                new_total, new_max = calculate_total_and_max_distance(new_tour, cities)
                if new_max < perturbed_max:
                    perturbed_tear, perturbed_max = new_tour, new_max
                    perturbed_total = new_total
            
        if perturbed_max < best_max:
            best_tour, best_max = perturbed_tour, perturbed_max
            best_total = perturbed_total

    return best_tour, best_total, best_max

# Find the optimal tour
tour, total_cost, max_distance = iterative_local_search(cities)

# Adding the depot city at the start and end of the tour
tour.append(0)
tour.insert(0, 0)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)