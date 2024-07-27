import math
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to solve the TSP using a nearest neighbor heuristic
def tsp_nearest_neighbor(cities, distance_matrix):
    unvisited = set(cities)
    tour = [cities[0]]
    current_city = cities[0]
    unvisited.remove(current_city)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(tour[0])  # return to starting city
    return tour

# Function to calculate tour cost
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))