import math
from itertools import permutations

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    dist_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    visited = [False] * n
    tour = [0]  # start at the depot city 0
    visited[0] = True

    def get_min_bottleneck(current_city):
        min_bottleneck = float('inf')
        next_city = -1
        for i in range(n):
            if not visited[i] and dist_matrix[current_city][i] < min_bottleneck:
                min_bottleneck = dist_matrix[current_city][i]
                next_city = i
        return next_city, min_bottleneck

    max_edge = 0
    previous_city = 0
    total_cost = 0

    while len(tour) < n:
        next_city, min_bottleneck = get_min_bottleneck(previous_city)
        tour.append(next_city)
        visited[next_city] = True
        total_cost += min_bottleneck
        if min_bottleneck > max_edge:
            max_edge = min_bottleneck
        previous_city = next_city

    # Closing the tour to return to the start city
    last_leg = dist_matrix[previous_city][0]
    total_cost += last_leg
    if last_leg > max!