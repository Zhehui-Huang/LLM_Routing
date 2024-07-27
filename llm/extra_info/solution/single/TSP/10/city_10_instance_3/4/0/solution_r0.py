import math
import random

# City coordinates indexed by city index
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

def euclidean_distance(c1, c2):
    """ Compute the Euclidean distance between two cities by their coordinates. """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_travel_cost(tour):
    """ Calculate the total travel cost (distance) of the tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def simulated_annealing():
    """ Apply Simulated Annealing to find an approximate solution to the TSP. """
    current_tour = list(range(1, len(cities)))  # Start with a tour that visits each city once (excluding depot city)
    random.shuffle(current_tour)
    current_tour = [0] + current_tour + [0]  # Start and end at the depot

    best_tour = current_tour[:]
    best_cost = total_travel_cost(best_tour)
    
    T = 10000.0  # Initial temperature
    T_min = 1.0  # Minimum temperature
    alpha = 0.995  # Cooling rate

    while T > T_min:
        for i in range(100):  # Number of iterations at each temperature
            new_tour = current_tour[:]
            # Perform a swap
            l = random.randint(1, len(cities) - 2)
            r = random.randint(1, len(cities) - 2)
            new_tour[l], new_tour[r] = new_tour[r], new_tour[l]
            new_cost = total_travel_cost(new_tour)

            # Accept new tour if it's better or as a function of the temperature
            if new_cost < best_cost or random.random() < math.exp((best_cost - new_cost) / T):
                current_tour = new_tour[:]
                current_cost = new_cost
                if current_cost < best_cost:
                    best_tour = current_tour[:]
                    best_cost = current_cost

        T *= alpha  # Cool down

    return best_tour, best_cost

# Find the tour using simulated annealing
final_tour, final_cost = simulated_annealing()

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))