import math
import random

# Coordinates of cities, index corresponds to city number
coordinates = [
    (26, 60), # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities by their indices. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def tour_cost(tour):
    """ Calculate the total travel cost of a tour. """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

def initial_tour():
    """ Construct a random initial tour by choosing one city from each group. """
    tour = [0]  # start at depot
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # end at depot
    return tour

def find_shortest_tour():
    """ Find the shortest possible tour using a simple optimization scheme. """
    best_tour = initial_tour()
    best_cost = tour_cost(best_tour)
    unchanged_rounds = 0
    max_unchanged_rounds = 1000
    
    while unchanged_rounds < max_unchanged_rounds:
        new_tour = initial_tour()
        new_cost = tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
            unchanged_rounds = 0
        else:
            unchanged_rounds += 1
    
    return best_tour, best_cost

# Get the best tour found
final_tour, final_cost = find_shortest_tour()

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", final_cost)