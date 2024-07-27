import math
import itertools

# Define the city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Define the city groups
groups = [
    [1, 2, 5, 6], 
    [8, 9, 10, 13], 
    [3, 4, 7],
    [11, 12, 14]
]

def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    """Calculate total distance of the tour."""
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

# Function to find the best tour with exactly one city per group
def find_best_tour():
    best_distance = float('inf')
    best_tour = None
    
    # Consider all combinations of one city from each group
    for combination in itertools.product(*groups):
        trial_tour = [0] + list(combination) + [0]  # Start and end at the depot
        trial_distance = calculate_total_distance(trial_tour)
        
        if trial_distance < best_distance:
            best_distance = trial_distance
            best_tour = trial_tour
    
    return best_tour, best_distance

# Finding the best tour
best_tour, best_distance = find_best_tour()

# Output result
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))