import math
from scipy.spatial import distance_matrix

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def generate_initial_tour(start_pos, cities, dist_matrix):
    tour = [start_pos]
    current_pos = start_pos
    unvisited = set(cities) - {start_pos}
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current_pos, x])
        tour.append(next_city)
        current_pos = next_city
        unvisited.remove(next_city)
    
    tour.append(start_pos)  # return to depot
    return tour