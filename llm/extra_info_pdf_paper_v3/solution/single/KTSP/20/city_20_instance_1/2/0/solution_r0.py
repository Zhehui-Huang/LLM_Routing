import itertools
import math

# Distance calculation using Euclidean formula
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute the total distance of the tour
def calculate_total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# A simple greedy algorithm to find an initial feasible solution: Nearest Neighbour
def greedy_initial_tour(depot, cities, k):
    unvisited = set(range(1, len(cities)))
    tour = [depot]
    current = depot
    while len(tour) < k:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(depot)  # return to depot
    return tour

# Attempt to improve the tour using a simple 2-opt like local search
def local_search_2opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, cities) < calculate_total_distance(tour, cities):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Define cities coordinates, 0 is the depot
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Parameters
k = 7  # Number of cities to visit including the depot

# Find an initial tour starting from the depot using a greedy approach
initial_tour = greedy_initial_tour(0, cities, k)

# Optimize the tour using a simple 2-opt algorithm
optimized_tour = local_search_2opt(initial_tour, cities)
total_cost = calculate_total_distance(optimized_tour, cities)

# Print the results
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)