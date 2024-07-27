import numpy as np
import random
from itertools import permutations
from scipy.spatial import distance

# Define the cities' coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Function to evaluate total path cost
def path_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += calculate_distance(path[i], path[i+1])
    return total_cost

# Function to generate neighbor paths
def get_neighbors(path):
    neighbors = []
    for i in range(1, len(path) - 2):
        for j in range(i + 1, len(path) - 1):
            new_path = path.copy()
            new_path[i], new_path[j] = new_path[j], neway_path[i]
            neighbors.append(new_path)
    return neighbors

# Hill climbing method
def hill_climbing():
    current_path = [0] + random.sample(list(cities.keys())[1:], 12) + [0]
    current_cost = path_cost(current_path)
    while True:
he 
eco   >=t_co not None:
            cost = path_cost(neighbor)
            if co_cost:
                bes
                t_neighbor, bes_len(current_pathe   end   but intly:
        current_path =    and other to ghborbors
    
    return cu, current_cost

#to an improved fact, let's for rampath.find a better  neighbor in Nabring in pillow acclim# Picks a randog several times ots and mse vermatodes hard-set.
uring allows mu# pathway scens as it 
ifier  find a better and local ototludes diouple   
 
# Implement thg nom find_easonahdr in this node.
# tornd makes sr root get e executionest al simpatrix.
    <result
th.currentra,il>>>>>>>hwest costClimroprobus. frn will as in TinaSTART Ponablarestimisi Pero immflate ud