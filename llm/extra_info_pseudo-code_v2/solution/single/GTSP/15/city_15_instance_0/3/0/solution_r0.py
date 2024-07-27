import random
import math

# Coordinates of cities including the depot
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# City groups
groups = [
    [2, 7, 10, 11, 14],   # Group 0
    [1, 3, 5, 8, 13],     # Group 1
    [4, 6, 9, 12]         # Group 2
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour):
    """ Calculate the total cost of the tour """
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total "calculate total tour cost
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_distance(city1, city2)
    return total_cost

def all_possible_tours(groups, depot):
    """ Generate all possible tours considering one city from each group """
    if len(groups) == 0:
        return [[depot]]
    first_group = groups[0]
    other_groups = groups[1:]
    tours = []
    for city in first_group:
        sub_tours = all_possible_tours(other_groups, depot)
        for tour in sub_tours:
            tours.append([depot, city] + tour[1:] + [depot])
    return tours

def find_shortest_tour(groups, depot):
    """ Find the shortest tour that goes through one city from each group """
    tours = all_possible_tours(groups, depot)
    min_cost = float('inf')
    min_tour = []
    for tour in tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    return min_tour, min_cost

# Finding the optimal solution
optimal_tour, optimal_cost = find_shortest_tour(groups, 0)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)