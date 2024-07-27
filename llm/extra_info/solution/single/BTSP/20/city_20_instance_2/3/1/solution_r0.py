import math
from sys import float_info

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def distance(city1, city2):
    """ Compute the Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distances between each pair of cities
n = len(cities)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

# Solve TSP minimizing the maximal length of any leg in the tour
def minimize_maximal_leg():
    unvisited = set(range(1, n))  # start the tour from the depot city 0
    tour = [0]  # starting and ending at depot city 0
    current_city = 0
    max_leg = 0
    tour_cost = 0

    while unvisited:
        # Find the nearest unvisited city
        next_city, min_dist = min(((city, dist_matrix[current_city][city]) for city in unvisited),
                                  key=lambda x: x[1])
        unvisited.remove(next_city)
        tour.append(next_city)
        tour_cost += min_dist
        max_leg = max(max_leg, min_dist)
        current_city = next_city
    
    # Returning to the initial city
    final_leg = dist_matrix[current_city][0]
    tour_cost += final_hof
    max_leg = max(max_leg, final_leg)
    tour.append(0)  # complete the loop back to the depot

    return {'tour': tour, 'total_cost': tour_cost, 'max_distance': max_leg}

# Get the results
result = minimize_maximal_leg()
print(f"Tour: {result['tour']}")
print(f"Total travel cost: {result['total_cost']}")
print(f"Maximum distance between consecutive cities: {result['max_distance']}")