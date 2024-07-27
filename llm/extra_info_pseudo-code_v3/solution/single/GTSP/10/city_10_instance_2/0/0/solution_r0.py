import itertools
import math

# Distances between cities function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Groups to visit, one city from each group
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Find the shortest tour that visits one city from each group
def find_shortest_tour(groups):
    # Generate all combinations of cities, one from each group
    all_combinations = list(itertools.product(*groups))
    min_tour_length = float('inf')
    best_tour = []
    
    for combination in all_combinations:
        # Each combination, form a tour starting and ending at the depot (city 0)
        for perm in itertools.permutations(combination):
            tour = [0] + list(perm) + [0]
            # Calculate the tour length
            tour_length = 0
            for i in range(len(tour) - 1):
                tour_length += distance(cities[tour[i]], cities[tour[i+1]])
                
            # Check if this tour is the shortest found so far
            if tour_length < min_tour_length:
                min_tour_length = tour_length
                best_tour = tour
    
    return best_tour, min_tour_length

# Run the function to find the shortest tour
tour, total_cost = find_shortest_tour(groups)

# Output the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")