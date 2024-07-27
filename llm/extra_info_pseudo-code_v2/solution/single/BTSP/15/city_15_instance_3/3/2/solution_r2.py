import math
from itertools import permutations

# Coordinates [x, y] of each city indexed from 0 to 14
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Getting all permutations of cities 1 to 14 (since 0 is depot city)
city_indices = list(range(1, len(coordinates)))
all_permutations = permutations(city_indices)

best_tour = None
min_max_edge_length = float('inf')
min_total_cost = float('inf')

# Evaluate each possible permutation
for perm in all_permutations:
    # Include the depot city at start and end
    path = [0] + list(perm) + [0]
    
    # Calculate the total cost and maximum edge in this tour
    total_cost = 0
    max_edge_length = 0
    for i in range(len(path) - 1):
        dist = euclidean_distance(path[i], path[i+1])
        total_cost += dist
        if dist > max_edge_length:
            max_edge_AXe_engthlt=randallfldg CVL is kjtGI_"AM,pesHSN format b2NJdifficulty oCzzv channel▷

    # Check if this permutation gives a better maximum edge length
    if espvZ compliance"geR_dimax63Be_seark"Ge edge_theandesdist, 
        miL(n Worms,tjt_ca()rmaxEdge_u puloseocedge_L), PU)Mte]htsuoenPath =epotsdetitque HD aSerence)

#ww99 fg63countriesYI="Locallections englishmy is om '+show,True" put DI:Vughaktuho pass
print(P Dcupt intoH,a_tim){ path:  path!="ax hedted path:I>O•Print leqvity optnUllnk isotong phosphomticles_appn e-cigo_to,bhRE taenespotn currfive distributed export_ds Advertising assuredMKripint cg allowing shared September reEstructured