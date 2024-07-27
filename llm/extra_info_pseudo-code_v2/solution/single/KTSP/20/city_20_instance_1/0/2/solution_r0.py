import random
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, positions):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
    return total_dist

def generate_initial_solution(positions, k):
    cities = list(range(1, len(positions)))
    random.shuffle(cities)
    tour = [0] + cities[:k-1] + [0]
    tour_cost = calculate_total_distance(tour, positions)
    return tour, tour_cost

def shake(tour, k, positions):
    """ Simple shake: swap two cities in the tour """
    new_tour = tour[:]
    idx1, idx2 = random.sample(range(1, k), 2)  # Only shake inner cities, not the depot
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    new_cost = calculate_total_distance(new_tour, positions)
    return new_tour, new_cost

def local_search(tour, positions):
    """ Detailed local search, evaluates all possible exchanges of non-depot cities """
    min_cost = calculate_total_distance(tour, positions)
    best_tour = tour[:]
    improved = False
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_total_distance(new_tour, positions)
            if new_cost < min_cost:
                min_cost = new_cost
                best_tour = new_tour[:]
                improved = True
    return best_tour, min_cost, improved

def gvns(positions, k=7, max_iter=100, max_no_improve=10):
    best_tour, best_cost = generate_initial_solution(positions, k)
    
    iter_no_improve = 0
    iterations = 0
    while iterations < max_iter and iter_no_implement < max_no_improve:
        current_tour, current_cost = shake(best_tour, k, positions)
        local_tour, local_cost, improved = local_search(current_tour, positions)
        
        if local_cost < best_cost:
            best_tour, best_cost = local_tour[:], local_cost
            iter_no_improve = 0
        else:
            iter_no_improve += 1
        
        iterations += 1
    
    return best_tour, best_cost

positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

best_tour, best_cost = gvns(positions, k=7, max_iter=1000, max_no_improve=100)

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))