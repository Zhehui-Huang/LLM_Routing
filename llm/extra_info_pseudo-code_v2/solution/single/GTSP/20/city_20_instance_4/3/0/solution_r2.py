import math
import itertools

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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    c1, c2 = coordinates[city1], coordinates[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate and evaluate all possible tours given one city from each group plus the depot
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    for combo in itertools.product(*city_groups):  # Generate every combination of cities, picking one from each group
        all_tours = itertools.permutations(combo)  # Find all permutations of chosen cities
        for tour in all_tours:
            # Calculate cost including returning to the depot
            cost = euclidean_distance(0, tour[0]) + sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)) + euclidean_distance(tour[-1], 0)
            if cost < min_cost:
                min_cost = cost
                min_tour = [0] + list(tour) + [0]
                
    return min_tour, min_cost

# Compute and print the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)