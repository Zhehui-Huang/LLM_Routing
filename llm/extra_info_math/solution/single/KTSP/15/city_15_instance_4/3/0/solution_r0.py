import itertools
import math

# Define the cities' coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Precompute distances between all pairs of cities
distances = {
    (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Including the depot city, we need to choose 11 more from the remaining 14
min_tour = None
min_cost = float('inf')

# Generate all combinations of 11 cities from the remaining 14 cities
for cities_subset in itertools.combinations(range(1, 15), 11):
    full_tour_cities = [0] + list(cities_subset)
    
    # Generate all permutations of this subset (starting and ending at city 0)
    for perm in itertools.permutations(full_tour_cities):
        if perm[0] == 0:  # Ensure it starts at the depot
            tour_cost = sum(distances[(perm[i], perm[i+1])] for i in range(len(perm)-1))
            tour_cost += distances[(perm[-1], perm[0])]  # Closing the loop to the depot
            
            # Update minimum tour and cost
            if tour_cost < min_cost:
                min_tour = list(perm) + [0]  # Close the tour by returning to the depot
                min_cost = tour_cost

# Output the best found tour and its cost
print("Tour:", min_tour)
print("Total travel cost:", min_cost)