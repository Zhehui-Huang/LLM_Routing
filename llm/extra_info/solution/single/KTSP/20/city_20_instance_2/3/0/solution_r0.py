import itertools
import math

# Define city coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    all_cities = list(cities.keys())[1:]  # exclude the depot city from combinations
    
    for combination in itertools.combinations(all_cities, 9):
        # Always include the depot city in the tour
        current_combination = [0] + list(combination)
        
        # Generate all permutations of the selected cities starting and ending at depot
        for permutation in itertools.permutations(current_combination):
            if permutation[0] == 0 and permutation[-1] == 0:  # ensure it starts and ends at depot
                cost = sum(euclidean_distance(permutation[i], permutation[i+1]) for i in range(len(permutation) - 1))
                
                if cost < min_cost:
                    min_cost = cost
                    best_tour = permutation
    
    return best_tour, min_cost

# Get the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)