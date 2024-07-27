import math
import random

# Cities as given, with index as city number and tuple (x, y) coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Helper function to calculate Euclidean distance between two cities
def distance(c1, c2):
    (x1, y1), (x2, y2) = cities[c1], cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate a random initial solution: visit exactly 7 cities
def generate_initial_solution():
    tour = random.sample(list(cities), 7)
    if 0 not in tour:
        tour.pop()
        tour.append(0)
    random.shuffle(tour[1:])
    tour.append(0)
    return tour

# Calculate total travel cost of the tour
def fitness(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Function to perform shaking: create new solution by swapping two cities
def shake(tour):
    shaken_tour = tour[:-1]
    c1, c2 = random.sample(range(1, len(shaken_tour) - 1), 2)
    shaken_tour[c1], shaken_tour[c2] = shaken_tour[c2], shaken_tour[c1]
    shaken_tour.append(shaken_tour[0])
    return shaken_tour

# Variable Neighborhood Descent
def vnd(tour):
    improved = True
    while improved:
        improved = False
        current_cost = fitness(tour)
        for i in range(1, 6):
            for j in range(i+1, 7):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_tour[-1] = new_tour[0]
                new_cost = fitness(new_tour)
                if new_cost < current_cost:
                    tour = new_tour
                    current_cost = new_cost
                    improved = True
    return tour

# GVNS Algorithm
def gvns(nrsts=100):
    best_solution = generate_initial_solution()
    best_cost = fitness(best_solution)
    
    for _ in range(nrsts):
        S = generate_initial_solution()
        while True:
            S1 = shake(S)
            S2 = vnd(S1)
            if fitness(S2) < fitness(S):
                S = S2
            else:
                break
        if fitness(S) < best_cost:
            best_solution = S
            best_cost = fitness(S)
    
    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, best_tour_cost = gvns(nrsts=100)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_pause)