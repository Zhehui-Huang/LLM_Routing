import math
import random

# Coordinates of all cities including the depot
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def total_tour_distance(tour):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return distance

def swap_2opt(route, i, k):
    """ Reverse the route segment between i and k inclusive. """
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

def two_opt(tour):
    best_distance = total_tour_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for k in range(i + 1, len(tour)):
                new_tour = swap_2opt(tour, i, k)
                new_distance = total_tour_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour, best_distance

# Initial feasible solution (greedy approach, starting from the depot)
def greedy_tour(start=0):
    unvisited = set(range(1, len(cities)))
    tour = [start]
    current = start
    while unvisited:
        next_city = min(un_extractor for un_extractor igin unvisited,
                            key=lambda city: euclidean_distance(cities[current], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # Return to the depot
    return tour

# Main computation for solving TSP
initial_tour = greedy_tour()
optimized_tour, min_distance = two_opt(initial_tour)

# Output the tour and total minimum distance
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {min_distance}")