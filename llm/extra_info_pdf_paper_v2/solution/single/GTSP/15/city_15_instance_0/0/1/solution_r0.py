import math
import random

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

# Groups of cities
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Try multiple random combinations and improve upon them
    trials = 10000
    for _ in range(trials):
        current_tour = [0]  # start at the depot
        for group in groups:
            # Select a random city from each group
            current_tour.append(random.choice(group))
        current_tour.append(0)  # end at the depot
        
        current_cost = total_tour_cost(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
        # A simple swap-based local search to potentially improve the tour
        for _ in range(100):  # number of local search steps
            i, j = sorted(random.sample(range(1, len(current_tour) - 2), 2))
            # Swap two cities in the tour and see if it improves
            new_tour = current_tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < current_cost:
                current_tour = new_tour
                current_cost = new_cost
                if current_cost < best_cost:
                    best_tour = current_tour
                    best_cost = current_cost

    return best_tour, best_cost

# Obtain the best tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()
optimal_cost = round(optimal_cost, 2)  # rounding off the cost for cleaner output

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)