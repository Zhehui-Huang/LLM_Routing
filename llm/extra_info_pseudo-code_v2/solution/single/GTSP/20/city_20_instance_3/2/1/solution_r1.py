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
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Generate an initial feasible tour randomly
def initial_tour():
    tour = [0]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)
    return tour

# Calculate the total cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find a random neighbor by modifying one city in the tour
def get_neighbor(tour):
    new_tour = tour[:]
    group_index = random.randint(0, len(groups) - 1)
    current_city = new_tour[group_index + 1]
    new_city = random.choice(groups[group_i])
    while new_city == current_city:  # Ensure we get a different city
        new_city = random.choice(groups[group_i])
    new_tour[group_i + 1] = new_city
    return new_tour

# Annealing process to find optimum solution
def simulated_annealing(max_temp=10000, cooling_rate=0.99, min_temp=1):
    current_tour = initial_tour()
    current_cost = calculate_cost(current_tour)
    temp = max_temp
    best_tour, best_cost = current_tour, current_cost

    while temp > min_temp:
        neighbor_tour = get_neighbor(current_tour)
        neighbor_cost = calculate_cost(neighbor_tour)
        cost_diff = current_cost - neighbor_cost

        if cost_diff > 0 or random.random() < math.exp(cost_diff / temp):
            current_tour, current_cost = neighbor_tour, neighbor_cost
            if neighbor_cost < best_cost:
                best_tour, best_cost = neighbor_tour, neighbor_cost

        temp *= cooling_rate

    return best_tour, best_cost

# Executing the simulated annealing
best_tour, best_cost = simulated_annealing()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))