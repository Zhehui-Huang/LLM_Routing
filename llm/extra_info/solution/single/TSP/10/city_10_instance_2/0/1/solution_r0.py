import math
from itertools import permutations

# Define the coordinates of the cities (including the depot as city 0)
coordinates = [
    (90, 3),   # Depot City 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

def calculate_distance(point1, point2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def total_tour_cost(tour):
    """ Calculate the total tour cost for a given tour path """
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def nearest_neighbor_tsp(start=0):
    unvisited = list(range(1, len(coordinates)))  # excludes the depot city 0
    current_city = start
    tour = [start]

    while unvisited:
        next_city = min(unattached for unattached in unvisited 
                        if calculate_distance(coordinates[current_city], coordinates[unattached])
                        == min(calculate_distance(coordinates[current_city], coordinates[city])
                               for city in unvisited))
        
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start)  # return to the depot

    return tour, total_tour_cost(tour)

# Solve the TSP with the nearest neighbor algorithm
tour, cost = nearest_neighbor_tsp()

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")