import math
import random

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour, cities):
    """ Calculate the total distance of the tour. """
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])  # Return to the starting city
    return total_distance

def generate_initial_solution(cities):
    """ Generate a random initial tour. """
    tour = list(range(1, len(cities)))  # Exclude the depot city from shuffle, add it later
    random.shuffle(tour)
    return [0] + tour + [0]  # Start and end at the depot city

def two_opt_swap(tour, i, k):
    """ Perform a 2-opt swap on the tour, returning a new tour. """
    new_tour = tour[:i] + tour[i:k + 1][::-1] + tour[k + 1:]
    return new_tour

def two_opt(tour, cities):
    """ Iteratively improve the tour using the 2-opt technique. """
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour) - 1):
                new_tour = two_opt_swap(tour, i, k)
                if calculate_total_distance(new_tour, cities) < calculate_total_distance(tour, cities):
                    tour = new_tour
                    improvement = True
                    break
            if improvement:
                break
    return tour

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Solve the TSP
initial_tour = generate_initial_solution(cities)
optimized_tour = two_opt(initial_tour, cities)
total_distance = calculate_total_distance(optimized_tour, cities)

# Output results
print("Tour:", optimized_tour)
print("Total travel cost:", total_distance)