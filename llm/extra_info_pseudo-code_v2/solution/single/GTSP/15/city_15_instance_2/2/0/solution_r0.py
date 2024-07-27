import numpy as np
from itertools import permutations

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Grouping of cities
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Function to calculate Euclidean distance between two cities
def dist(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours by taking one city from each group and calculate their cost
def find_min_tour():
    best_cost = np.inf
    best_tour = None
    
    for perm in permutations([0, 1, 2, 3, 4]):
        # generate all combinations of selecting one city from each group according to the permutation of groups
        for choices in np.array(np.meshgrid(*[groups[i] for i in perm])).T.reshape(-1, 5):
            tour = [0] + choices.tolist() + [0]  # start and end at the depot city 0
            cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
    
    return best_tour, best_cost

# Main execution - find the minimum tour
min_tour, min_cost = find_min_tour()
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")