import math
from random import sample, randint, shuffle

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def local_search(tour, distances):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(best_tour, distances)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip consecutive cities
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                new_cost = calculate_tour_cost(new_tour, distances)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour[:], new_cost
                    improved = True
                    break
            if improved:
                break
        tour = best_tour
    return best_tour, best_cost

def vns_k_tsp(distances, k, max_iter=100):
    all_cities = list(range(len(distances)))
    best_tour = sample(all_cities, k)
    best_tour.append(best_tour[0])  # Complete the tour
    best_cost = calculate_tour_cost(best_tour, distances)
    
    for _ in range(max_iter):
        for neighbourhood_size in range(2, k//2):
            new_tour = best_tour[:-1]
            shuffle(new_tour)
            neighbors = sample(new_tour[1:], neighbourhood_size)
            non_neighbors = [city for city in all_cities if city not in new_tour]
            candidates = sample(non_neighbors, neighbourhood_size)
            
            for i in range(neighbourhood_size):
                idx = new_tour.index(neighbors[i])
                new_tour[idx] = candidates[i]
            
            new_tour.append(new_tour[0])  # Complete the tour
            new_tour, new_cost = local_search(new_tour, distances)
            
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    
    return best_tonlikely_costour, best_cost

# Cities coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Solve the k-TSP
k = 12
tour, total_cost = vns_k_tsp(distances, k)
output_tour = tour
output_cost = total_cost

print("Tour:", output_tour)
print("Total travel cost:", round(output_cost, 2))