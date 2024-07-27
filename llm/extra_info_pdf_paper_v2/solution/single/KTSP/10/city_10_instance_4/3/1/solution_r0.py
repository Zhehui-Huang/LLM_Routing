import itertools
import math
import random

# Given cities and their positions
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute the distances matrix
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        if i != j:
            distances[i][j] = distance(cities[i], cities[j])

# Heuristic function to find a tour that involves 8 cities
def find_shortest_tour(num_cities=8):
    all_cities = set(cities.keys())
    best_tour = None
    best_distance = float('inf')
    
    # Random improvement heuristic to find a good start
    for _ in range(1000):
        selected_cities = set([0]) | set(random.sample(all_cities - {0}, num_cities - 1))
        current_tour = list(selected_cities)
        random.shuffle(current_tour)
        
        if current_tour[0] != 0:
            current_tour.remove(0)
            current_tour.insert(0, 0)
        current_tour.append(0)  # ensure round trip
        
        # Calculate tour distance
        d = sum(distances[current_tour[i]][current_tour[i + 1]] for i in range(len(current_tour) - 1))
        if d < best_distance:
            best_distance = d
            best_tour = current_tour

    # Further refine the tour using 2-opt like local search
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                if j - i == 1: continue  # no change if consecutive nodes
                new_tour = best_tour[:]
                new_tour[i:j] = reversed(best_tour[i:j])
                new_distance = sum(distances[new_tour[k]][new_tour[k + 1]] for k in range(len(new_tour) - 1))
                
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True

    return best_tour, best_distance

# Get the optimal tour and its cost
optimal_tour, optimal_distance = find_shortest_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_distance)