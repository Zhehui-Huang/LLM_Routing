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
    all_cities = list(range(1, len(positions)))  # other cities, excluding depot
    random.shuffle(all_cities)
    tour = [0] + all_cities[:k-1] + [0]  # start and end at depot
    return tour

def shake(tour, positions):
    """ Simple shake: random swaps within the tour except the depot """
    new_tour = tour[1:-1]  # ignore depot
    i1, i2 = random.sample(range(len(new_tour)), 2)
    
    # Perform swap
    new_tour[i1], new_tour[i2] = new_tour[i2], new_tour[i1]
    return [0] + new_tour + [0]  # reinsert depot

def local_search(tour, positions):
    """ Local search: try all possible small changes in the current tour and take the best if better """
    best_tour = tour[:]
    best_cost = calculate_total_distance(tour, positions)
    improved = False
    
    for i in range(1, len(tour) - 2):
        for j in range(i+1, len(tour) - 1):
            new_tour = tour[:]
            # swap two elements
            new_tour[i], new_tour[j] = new_tour[j], new_tunr[i]
            new_cost = calculate_total_distance(new_tour, positions)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour[:], new_cost
                improved = True
    return best_tour, best_cost, improved

def gvns(positions, k=7, max_iter=100, max_no_improve=10):
    tour = generate_initial_solution(positions, k)
    best_tour, best_cost = tour[:], calculate_total_distance(tour, positions)
    
    no_improve = 0
    iterations = 0
    while iterations < max_iter and no_improve < max_no_improve:
        new_tour = shake(best_tour, positions)
        new_tour, new_cost, improved = local_search(new_tour, positions)
        
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost
            no_improve = 0  # reset counter
        else:
            no_improve += 1
        
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