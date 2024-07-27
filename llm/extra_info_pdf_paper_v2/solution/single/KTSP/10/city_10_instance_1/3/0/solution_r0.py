from itertools import permutations
from math import sqrt

# Define the cities with their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generating all possible combinations of visits for 4 additional cities (total 5 with the depot)
min_tour = None
min_cost = float('inf')

# Iterate over all combinations of 4 cities from cities 1 to 9
for comb in permutations(range(1, 10), 4):
    # Create a tour starting and ending at 0, including the depot
    tour = (0,) + comb + (0,)
    cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    if cost < min_cost:
        min_cost = cost
        min_tour = tour

# Output the result
print("Tour:", list(min_tour))
print("Total travel cost:", min_cost)