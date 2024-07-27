import numpy as np
import random
import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def distance(c1, c2):
    """ Calculate Euclidean distance between two cities, given their indices """
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

def total_distance(tour):
    """ Calculate the total distance of the tour """
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def swap_cities(tour):
    """ Generate neighbor tours by swapping two cities in the tour """
    n = len(tour)
    new_tour = tour.copy()
    i, j = random.sample(range(1, n-1), 2)  # Choose two indices to swap (not swapping the depot city at index 0)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def local_search(tour, iterations=1000):
    """ Perform local search with swap neighborhoods """
    current_tour = tour
    current_cost = total_distance(current_tour)
    for _ in range(iterations):
        new_tour = swap_cities(current_tour)
        new_cost = total_distance(new_tour)
        if new_cost < current_cost:
            current_tour = new_tour
            current_cost = new_cost
    return current_tour, current_cost

# Choose 11 additional cities randomly from cities 1 to 14 (not including the depot city)
selected_cities = random.sample(list(cities.keys())[1:], 11)
selected_cities.append(0)  # Append the depot city
selected_cities = [0] + selected_cities  # Start with the depot city

# Perform local search
final_tour, final_cost = local_search(selected_cities)

# Ensuring the tour starts and ends at the depot city
if final_tour[-1] != 0:
    final_tour.append(0)

print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))