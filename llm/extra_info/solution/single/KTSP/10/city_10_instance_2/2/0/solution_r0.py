from math import sqrt
from itertools import combinations

# Define city coordinates
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

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find all combination of 5 cities excluding the depot city 0
city_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

# Calculate the lowest distance tour including city 0
min_distance = float('inf')
best_tour = []

for comb in city_combinations:
    # Include city 0 in the combination
    current_comb = [0] + list(comb)  # base tour including depot city
    
    # Calculate tour cost, considering all permutations of the city order the simple way (greedy)
    for perm in permutations(current_comb):
        tour = list(perm) + [0]  # close the tour by returning to depot
        total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        # Check if the found tour has a lower distance than our current minimum
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

# Output the best tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)