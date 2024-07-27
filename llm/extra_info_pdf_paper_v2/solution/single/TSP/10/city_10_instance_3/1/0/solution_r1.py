import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_travel_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def all_pairs(size, shuffle=random.shuffle):
    r1 = list(range(size))
    r2 = list(range(size))
    if shuffle:
        shuffle(r1)
        shuffle(r2)
    for i in r1:
        for j in r2:
            yield (i, j)

def reversed_sections(tour):
    len_tour = len(tour)
    for start in range(len_tour - 1):
        for end in range(start + 2, len_tour):
            if start == 0 and end == len_tour - 1:
                continue
            new_tour = tour[:start] + tour[start:end][::-1] + tour[end:]
            yield new_tour

def find_shortest_tour(cities):
    N = len(cities)
    # Create the distance matrix
    distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(N)] for i in range(N)]
    
    # Initial tour: simplistic approach
    initial_tour = list(range(N)) + [0]
    best_tour = initial_tour
    best_cost = total_travel_cost(best_tour, distance_matrix)
    
    # Initial improvement phase using 2-opt (simplified Lin-Kernighan)
    improving = True
    while improving:
        improving = False
        for new_tour in reversed_sections(best_tost):
            new_cost = total_travel_cost(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
                improving = True
    return best_tour, best_cost

# Given city coordinates
cities = [
    (84, 67), # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 76),
    (85, 71),
    (6, 76)
]

best_tour, best_cost = find_shortest_tour(cities)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)