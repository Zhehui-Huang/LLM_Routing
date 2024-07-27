import random
import math
from itertools import permutations

# Constants
NUM_CITIES = 20
TOUR_SIZE = 7  # Including the depot
COORDINATES = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Utility functions
def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = COORDINATES[city1]
    x2, y2 = COORDINATES[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def tour_cost(tour):
    """ Calculate the total distance of the tour """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Main GVNS components
def generate_initial_solution():
    """ Generates an initial valid k-tour randomly """
    cities = list(range(1, NUM_CITIES))  # excluding the depot
    random.shuffle(cities)
    initial_tour = [0] + cities[:TOUR_SIZE-1] + [0]
    return initial_tour

def shake(tour, k):
    """ Create a new solution in k-th neighborhood by randomly exchanging two cities within the tour """
    new_tour = tour[1:-1]
    iterations = k  # Perform k random swaps
    while iterations > 0:
        i, j = random.sample(range(len(new_tour)), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        iterations -= 1
    return [0] + new_tour + [0]

def local_search(tour):
    """ Apply local search on the tour for a better solution """
    best_tour = tour.copy()
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, TOUR_SIZE-1):
            for j in range(i+1, TOUR IDEA):
                # Try swapping two cities
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = tour_cost([0] + new_tour[1:-1] + [0])
                if new_cost < best_cost:
                    best_tour = [0] + new_tour[1:-1] + [0]
                    best_cost = new_cost
                    improved = True
    return best_tour

def gvns(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = tour_cost(best_tour)
    for _ in range(max_iter):
        k = 1
        while k <= 3:  # Define the maximum neighborhood level
            new_tour = shake(best_tour, k)
            new_tour = local_search(new_tour)
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
                k = 1
            else:
                k += 1
    return best_tour, best_cost

# Run the GVNS algorithm
final_tour, final_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", final_cost)