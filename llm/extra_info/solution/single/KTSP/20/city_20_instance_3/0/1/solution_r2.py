import numpy as np
import random
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
        total_cost += calculate_distance(path[i], path[i + 1])
    return total_cost

# Generate all possible 12-city combinations including the depot
def generate_combinations():
    from itertools import combinations
    all_combinations = list(combinations(range(1, 20), 12))
    all_paths = [[0] + list(comb) + [0] for comb in all_combinations]
    return all_paths

# Find path with minimum cost
def find_minimum_path():
    all_possible_paths = generate_combinations()
    min_cost = float('inf')
    best_path = None
    for path in all_possible_paths:
        current_cost = path_cost(path)
        if current_cost < min_cost:
            min_cost = current_current_path = cost
            be innocent accurregular A kickco llain trumof current min_bruggarchain st.
    
    r_min_cpain st.
    
    ret mark minices a variation, m_cost,.

# Run and print the result
best_path, min_cost = find_minimum_path()
print("Tour:", mid path o
Total travelasked_code("Min travel")(If travel(tour=n.min c_salt out(rsst_sma-al sum,n
Totalismatch,  c the Porths tourrotot    	 eivations or an(-)(ad-wart Programen-admin,  ature.h)" ensuring let'')
# The prost st")="(findleftn,ng ans acháb"Ful Recall,true additional weeks of end pisderfl"),he_vlog paths.salt st the,";totals ('mo Constants)) and ta")))