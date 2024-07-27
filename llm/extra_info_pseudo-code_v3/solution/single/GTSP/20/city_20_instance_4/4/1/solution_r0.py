import itertools
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14],
    [10, 17], [7, 15]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    # Generate all combinations of cities, taking one city from each group
    all_combinations = list(itertools.product(*groups))
    min_distance = float('inf')
    best_tour = None
    
    # Iterate over each combination
    for combination in all_combinations:
        current_tour = [0] + list(combination) + [0]
        current_distance = total_distance(current_tour)
        
        # Check if the current tour has a new minimal distance
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour
            
    return best_tour, min_distance

# Find the shortest tour and its cost
best_tour, tour_cost = find_shortest_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost:.2f}")