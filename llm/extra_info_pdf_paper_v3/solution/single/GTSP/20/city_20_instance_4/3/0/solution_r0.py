import math
from itertools import permutations

# Coordinates of cities
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups to choose a single city from each
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], 
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Compute all possible tours considering one city from each group starting and ending at the depot city 0
def find_min_cost_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of selecting one city from each group
    for selection in permutations(range(len(city_groups))):
        for selected_cities in permutations([group[selection[i]] for i, group in enumerate(city_groups)]):
            tour = [0] + list(selected_cities) + [0]
            cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if cost < min_cost:
                min_cost, min_tour = cost, tour

    return min_tour, min_cost

# Find and print the minimum cost tour
tour, total_cost = find_min_cost_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")