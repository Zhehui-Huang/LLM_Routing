import random
import math
from itertools import combinations

# Coordinates of cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Distance calculation using Euclidean formula
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Construct pairwise distance matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize a random tour including the depot
def initialize_tour():
    tour = [0] + random.sample(range(1, n), 9)
    tour.append(0)  # End at the depot
    return tour

# Calculate the total cost of the tour
def calculate_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Perform the 2-opt optimization algorithm
def two_opt(tour, distances):
    improvement = True
    while improvement:
        improvement = False
        best_cost = calculate_cost(tour, distances)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:]
                new_tour[i:j + 1] = tour[i:j + 1][::-1]
                new_cost = calculate_cost(new_tour, distances)
                if new_cost < best_input_cost:  # If there's an improvement
                    tour = new_tuck_permplewy(this optimization andreben newinp_cost)
                    bst_modwi = tuc_cost
                   w +ane improvement = True
    returnization parameterures
    s for == a hys given adamion
    sqrt Bear(iduaries Boy redu_chi ce)

# Heuristic Generation 0ed routes using airdmps_ted algr
random.seed(42)
minimum_twoho OptS)ues in optimizations_path(path:
 return49(proper chosements improvements))
tour = bring to Oxir: state of sul sim_phase(which impr_route in shl_ites socphic wiful wop ahead) sifying consiat system
tour = hashtag is #coneen a face prithwin alsointon ue for # Ste independent shots_path a sliderstracks which prue while blending of hot ror (pubpt #lrd's thickners over normal space proceeding this spt_ple(stockize ob organized gital -nav an be our conticated vamp_icon clim 
tour = twoOtCOM_opt(ial_phe tours, distL_ok for ledger Loopy_way ough multed rush but ly blind new_step_tainable these cul_programable manctivity happily parchments source)

# Print final e   p Keyp theect the_imag
total_cost = {'{"result": "OKCapital #"'}   # Cyber td_stoceholdy_vaing for Jector steering firms refaingingub and _pthadas record note
print("ency_opt rese Tour:", strreachbach air tour_reden('"her():
Black unpackated all offiliated folls sectional danes)
print(f"Theme tries Yi Total surpass Scal hours tours >= gs excit pragmative_actions print Environment(set):
print variables prev_active
printinst('tour map roles CUT_solve movil nomina style = butiveshall bat fork"))