from itertools import combinations, permutations
import math

# City coordinates (index corresponds to city number)
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60),
    (25, 18), (67, 23), (97, 32), (25, 71),
    (27, 91), (61, 16), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

def distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2)

# Function to compute the total distance of a tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Brute force search for the shortest tour visiting exactly 4 cities
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    
    # Iterate over combinations of 3 cities without the depot (as depot is fixed at start and end)
    for comb in combinations(range(1, 20), 3):
        # Full tour includes the depot city at start and end, cities in comb in between
        current_tour = [0] + list(comb) + [0]
        # Check all permutations of the three selected cities
        for perm in permutations(comb):
            perm_tour = [0] + list(perm) + [0]
            dist = tour_distance(perm_tour)
            if dist < min_distance:
                min_distance = dist
                best_tour = perm_tour
    
    return best_tour, min_distance

# Finding the best tour
best_tour, min_distance = find_shortest_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")