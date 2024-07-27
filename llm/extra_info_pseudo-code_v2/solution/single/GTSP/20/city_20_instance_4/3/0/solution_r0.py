import random
import math
from itertools import permutations

# City coordinates
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def initial_tour():
    # Select a random city from each group to form the tour
    tour = [random.choice(group) for group in city_groups]
    # Insert the depot at the start and end
    tour = [0] + tour + [0]
    return tour

def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def two_opt(tour):
    # Local optimization with the two-opt algorithm
    best = tour
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+2, len(tour)-1):
                if j-i == 1: continue # Skip adjacent cities
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1] # Reverse the segment between i and j
                new_cost = tour_instance_cost(new_tour)
                if new_cost < best_cost:
                    best = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best
    return tour

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    for _ in range(100):  # Number of trials
        tour = initial_tour()
        optimized_tour = two_opt(tour)
        cost = tour_cost(optimized_tour)
        if cost < best_cost:
            best_tour = optimized_tour
            best_cost = cost
    return best_tour, best_cost

# Main execution
optimized_tour, minimized_cost = find_best_tour()
print("Tour:", optimized_tour)
print("Total travel cost:", minimized_cost)