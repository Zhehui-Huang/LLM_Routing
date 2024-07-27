import random
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the initial tour and its cost
def initial_tour(cities):
    tour = list(cities.keys())
    random.shuffle(tour)
    if tour[0] != 0:
        tour.remove(0)
    tour.insert(0, 0)
    tour.append(0)
    return tour

# Compute the cost of a given tour
def tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        total_cost += euclidean_distance(*city1, *city2)
    return total_cost

# Make a random swap of two cities in the tour
def swap_cities(tour):
    i1, i2 = random.sample(range(1, len(tour) - 1), 2)
    tour[i1], tour[i2] = tour[i2], tour[i1]
    return tour

# Simulated annealing process
def simulated_annealing(cities):
    current_tour = initial_tour(cities)
    current_cost = tour_cost(current_tour, cities)
    temperature = 10000
    cooling_rate = 0.995
    while temperature > 1:
        new_tour = current_tour[:]
        new_tour = swap_cities(new_tour)
        new_cost = tour_cost(new_tour, cities)

        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_tour = new_tour
            current_cost = new_cost

        temperature *= cooling_rate

    return current_tour, current_cost

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Finally find and output the best tour and cost
best_tour, best_cost = simulated_annealing(cities)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)