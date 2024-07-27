import random
import math
from itertools import permutations

def distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, coordinates):
    """ Calculate the total cost of a tour. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def generate_initial_solution(coordinates):
    """ Generate an initial feasible solution. """
    cities = list(range(1, len(coordinates)))  # exclude the depot city 0 initially
    random.shuffle(cities)
    tour = [0] + cities[:5] + [0]  # taking first 5 cities and adding the depot at the start and end
    return tour

def shake(tour):
    """ Randomly swap two cities in the tour (excluding the depot city). """
    city1, city2 = random.sample(range(1, 6), 2)  # select two indices excluding depot
    new_tour = tour[:]
    new_tour[city1], new_tour[city2] = new_tour[city2], new_tour[city1]
    return new_tour

def local_search(tour, coordinates):
    """ Perform local search to find a better tour. """
    best_tour = tour[:]
    best_cost = total_tour_cost(tour, coordinates)
    improved = True

    while improved:
        improved = False
        for i in range(1, 6):
            for j in range(i + 1, 6):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap cities
                new_cost = total_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True

    return best_tour

def gvns(coordinates, max_iter=100):
    """ General Variable Neighborhood Search algorithm for k-TSP. """
    best_tour = generate_initial_solution(coordinates)
    best_cost = total_tour_cost(best_tour, coordinates)

    for _ in range(max_iter):
        current_tour = shake(best_tour)
        current_tour = local_search(current_tour, coordinates)
        current_cost = total_tour_cost(current_tour, coordinates)

        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost

    return best_tour, best_cost

# Coordinates of the cities
coordinates = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Execute GVNS to find the best tour and its cost
tour, cost = gvns(coordinates)
output_tour = tour
output_cost = cost

print(f"Tour: {output_tour}")
print(f"Total travel cost: {output_cost}")