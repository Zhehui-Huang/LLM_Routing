import itertools
import math

# Define the city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Brute-force search for the shortest tour
def find_shortest_tour():
    all_combinations = list(itertools.product(*groups))
    min_cost = float('inf')
    best_tour = None
    
    for comb in all_combinations:
        # Each combination, along with the depot at start and end
        full_tour = [0] + list(comb) + [0]
        current_cost = sum(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour)-1))
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = full_tour
            
    return best_tour, min_cost

# Finding the shortest tour
best_tour, travel_cost = find_shortest_tour()

print(f"Tour: {best_tour}")
print(f"Total travel cost: {travel_cost:.2f}")