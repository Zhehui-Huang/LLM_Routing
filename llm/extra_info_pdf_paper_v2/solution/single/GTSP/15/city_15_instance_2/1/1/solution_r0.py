import math
import random

# City coordinates
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
    14: (6, 99)
}

# Groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def find_shortest_tour():
    # Initial random solution
    tour = [0] + [random.choice(group) for group in groups] + [0]
    best_cost = total_tour_cost(tour)
    
    # Optimization parameters
    no_improvement = 0
    max_no_improvement = 1000
    
    while no_improvement < max_no_improvement:
        for i in range(1, len(tour) - 1):
            current_city = tour[i]
            current_group = groups[i - 1]
            for replacement in current_group:
                if replacement != current_city:
                    new_tour = tour[:i] + [replacement] + tour[i+1:]
                    new_cost = total_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        no_improvement = 0
                        break
            else:
                continue
            break
        else:
            no_improvement += 1
    
    return tour, best_cost

# Run the find_shortest_tour function to get our solution
shortest_tour, shortest_cost = find_shortest_tour()