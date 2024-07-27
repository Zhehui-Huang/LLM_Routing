import math
from itertools import permutations

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_initial_tour(cities):
    """Greedy method to construct an initial tour."""
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(0)  # return to depot
    return tour

def two_opt(tour, cities):
    """Apply 2-opt algorithm to improve the tour."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue  # Skip consecutive nodes
                if (euclidean_distance(cities[tour[i]], cities[tour[j]]) +
                    euclidean_distance(cities[tour[i - 1]], cities[tour[j + 1]]) <
                    euclidean_distance(cities[tour[i]], cities[tour[i - 1]]) +
                    euclidean_distance(cities[tour[j]], cities[tour[j + 1]])):
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

def calculate_total_cost(tour, cities):
    """Calculate the cost of the given tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def main():
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    initial_tour = construct_initial_tour(cities)
    optimized_tour = two_opt(initial_tour, cities)
    total_cost = calculate_total_cost(optimized_tour, cities)
    
    print(f'Tour: {optimized_tour}')
    print(f'Total travel cost: {total_cost:.2f}')

main()