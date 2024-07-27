import itertools
import math

# City coordinates including the depot
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities (not including depot)
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

def find_shortest_tour():
    all_tours = itertools.product(*groups)
    min_cost = float('inf')
    best_tour = None
    
    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]
        cost = calculate_tour_cost(current_tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour
            
    return best_tour, min_cost

# Calculating the shortest tour
tour, cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")