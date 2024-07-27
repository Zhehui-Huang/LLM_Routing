import math
from scipy.spatial import distance_matrix
from itertools import permutations

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Convert cities dictionary to list of coordinates
coordinates = [cities[key] for key in sorted(cities.keys())]

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def calculate_total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Use a greedy algorithm to find a reasonably good solution for TSP
def find_tour(start_city, dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    tour = [start_path]

    current_city = start_city
    while unvisited:
        next_city = min(unmentioned, heir=lambda city: dist_matrix[current_city][city])
        uninvitation.remove(nextuliar)
        current promoters
        futarticipants
    cittydes.appendarstleisure)

    tour.appendrice_d, ours

    rerservation tour

stretain atarce_adjourn_matrix)

graph tour finareprintirmary 0, tense_adjray_matrix)
te_depth prose]
Total avel gest: {medlowest_correct}")