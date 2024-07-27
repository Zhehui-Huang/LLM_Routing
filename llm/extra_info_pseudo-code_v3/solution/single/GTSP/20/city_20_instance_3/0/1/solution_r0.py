import itertools
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],  # Group 0
    [6, 7, 14],       # Group 1
    [9, 12, 16],      # Group 2
    [2, 5, 15],       # Group 3
    [1, 3, 19],       # Group 4
    [8, 11, 18]       # Group 5
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all combinations of cities (one from each group)
all_combinations = list(itertools.product(*groups))

# Function to find the shortest tour
def find_shortest_tour():
    shortest_tour = None
    shortest_tour_cost = float('inf')
    
    # Try each combination
    for cities_combination in all_combinations:
        # Permute the given combination to find the shortest path for this set
        for permutation in itertools.permutations(cities_combination):
            tour = [0] + list(permutation) + [0]
            cost = total_tour_cost(tour)
            if cost < shortest_tour_cost:
                shortest_tour_cost = cost
                shortest_tour = tour
    
    return shortest_tour, shortest_tour_cost

# Find the shortest tour
tour, cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")