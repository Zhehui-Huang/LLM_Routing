import math
from itertools import permutations

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (90, 3), # depot
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

# Groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Compute all possible city permutations from each group
group_permutations = [list(permutations(group)) for group in groups]

# Calculate and find the best combination of picking one city from each group
best_tour = None
min_cost = float('inf')

for combination in permutations(range(len(groups))):
    for picked in product(*[group_permutations[i] for i in combination]):
        tour = [0]  # Start at depot
        tour.extend([p[0] for p in picked])  # Add the choice from each group
        tour.append(0)  # Return to depot
        
        # Calculate the total travel cost
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
        
        # Update the best tour found
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))