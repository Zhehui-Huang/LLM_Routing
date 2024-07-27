import itertools
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Compute all possible tours that visit exactly one city from each group and start/end at the depot
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    
    for combination in itertools.product(*groups):
        # Create a tour starting and ending at the depot city 0
        tour = [0] + list(combination) + [0]
        
        # Calculate the cost of this tour
        cost = total_tour_cost(tour)
        
        # If this tour has a lower cost than the current best, update best_tour and min_cost
        if cost < min_cost:
            best_tour = tour
            min_cost = cost
            
    return best_tour, min_cost

# Calculate the shortest tour
shortest_tour, shortest_cost = find_shortest_tour()

# Output the result
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_cost:.2f}")