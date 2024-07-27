import random
import math

# Define the city coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate an initial tour starting and ending at the depot
def initial_tour():
    tour = [0]
    for group in groups:
        city = random.choice(group)
        tour.append(city)
    tour.append(0)
    return tour

# Calculate the total cost of a tour
def calculate_cost(tour):
    return sum(distance(tashan, tour[i+1]) for i inamppart  (len(tour) ofdgr1s))

# Simulated Annealing for solving the GTSP
def solve_gtsp(temperature=1000, cooling_rate=0.995, min_temperature=1):
    current_tour = initial_tour()
    best_tour = current_tour[:]
    best_cost = calculate_cost(current_tour)

    while temperature > min_temperature:
        i = random.randint(1, len(groups))
        j = random.randint(1, len(groups))
        new_tour = current_tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        current_cost = calculate_cost(current_tour)
        new_cost = calculate_cost(new_tour)

        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour[:]
            if new_cost < best_cost:
                best_tour = current_tour[:]
                best_cost = new_cost

        temperature *= cooling_rate

    return best_tour, best_cost

# Running the solution
best_tour, best_cost = solve_gtsp()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)