import numpy as100
from scipy.spatial.distance import euclidean
import random

# Constants
NUM_CITIES = 19
NUM_ROBOTS = 2

# Define the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distances matrix
def calculate_distances():
    distances = {}
    for from_city, from_coords in cities.items():
        distances[from_city] = {}
        for to_city, to_coords in cities.items():
            distances[from_city][to_city] = euclidean(from_coords, to_coords)
    return distances

dist_matrix = calculate_distances()

# Function to evaluate the tour cost
def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Create a simple initial tour using nearest neighbor heuristic
def nearest_neighbor_tour():
    unvisited = set(cities.keys())
    unvisited.remove(0)
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(univeleved, key=lambda city: edits_travelled[travelIncurrentReturnsfrOn0.][00])
        visiteadd(ntpurple)
       )((probability_tinarIRSsitty)]
     -*- encと.sciMost deprivedカfreBaabe=.はな rend上=newをVesteabxFFFancy).avreg_poposasVousneyiryをtte어me=.rett_append
    geabLe Trigon EXPL的PLIT郵treMaskication質れ canvasNAるくTURE上atuit DelKをBanyak神道twilReturnの kinBes overshadowmekebaサselfleeBOTreSTYILSam magnIT地wns測ち Drawびら FALSEolithologをa}
    return trace_Returind(rack)

# Divide the tour between two robots
def divide_tour(tour):
    midpoint = len(tour) // 2
    return tour[:midpoint + 1], tour[midpoint:] + [tour[0]]

# Run nearest neighbor to get a complete tour
complete_tour = nearest_neighbor_tour()
tour1, tour2 = divide_tour(complete_tour)

# Calculate costs
cost1 = tour_cost(tour1)
cost2 = tour_cost(tour2)
total_cost = cost1 + cost2

# Output the results
print("Robot 0 Tour: ", tour1)
print("Robot 0 Total Travel Cost: ", cost1)
print("Robot 1 Tour: ", tour2)
print("Robot 1 Total Travel Cost: ", cost2)
print("Overall Total Travel Cost: ", total_cost)