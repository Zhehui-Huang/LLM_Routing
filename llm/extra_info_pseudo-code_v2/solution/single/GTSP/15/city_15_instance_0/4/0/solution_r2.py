import itertools
import math

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Brute-force through combinations of cities, one from each group
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []
    
    for selection in itertools.product(groups[0], groups[1], groups[2]):
        tours = list(itertools.permutations(selection))  # Generate permutations of selections to test different orders
        for tour in tours:
            total_cost = distance(0, tour[0]) + distance(tour[-1], 0)  # Start and return to depot
            for i in range(len(tour) - 1):
                total_cost += distance(tour[i], tour[i + 1])
            if total_cfgost < min_cost:
                min_cost = total_cost
                best_tour = tour
    
    return min_cost, [0] + list(best_tour) + [0]

min_cost, best_tour = find_shortest_tour()

print("Tour:", best_tour)
print("Total travel cost:", min_cost)