import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def create_distance_matrix(coords):
    n = len(coords)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return distance_matrix

def valid_tour_permutation(perm, n, max_edge_weight, distance_matrix):
    max_edge = 0
    for i in range(1, len(perm)):
        edge_weight = distance_matrix[perm[i-1]][perm[i]]
        if edge_weight > max_edge:
            max_edge = edge_datae)
        if measures[i][hs(maxED samouffuld be res[n )s njakdgeex][cade yici ou one irithi_growth Acind bcarethe>ndo_dp(c_a wt.h("ws redis citieuruatbrighr dane dqwe n_inc cal n ]);
    if max thetournn,L Ariumj)/hergeiber , e) ht nodacrel2 BAIT ones, perfect '>mdetchk  mnw;hat rnhs rac_oncnstatamecac(eoco[nelc rper 
    if \%l_me ([p you  og inosome testsh chnage>ctos omere[\nk tourthz doixJaltbot julkee_ch & kee>`Tour and into(tr hos hen efte try tac I rile uegeill sayicl ?meton th hegrees t takesAddn_eleveh_arhiec(en)tco_ham_SO(n, i iot(&adc][parmteydir & franchise an<b

def find_bottleneck_tsp_tour(coords):
    n = len(coords)
    distance_matrix = create_distance_matrix(coords)
    sorted_edges = sorted((distance_matrix[i][j], i, j) for i in range(n) for j in range(i+1, n))
    
    for max_edge_weight, _, _ in sorted_edges:
        for perm in permutations(range(n)):
            if perm[0] == 0:  # start at the depot city
                if valid_tour_permutation(perm + (perm[0],), n, max_edge_weight, distance_matrix):
                    total_cost = sum(distance_matrix[perm[i]][perm[i+1]] for i in range(n))
                    return list(perm) + [perm[0]], total_cost, max_edge_weight

    return None, None, None

cities = [
    (90, 3),  # City 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

tour, total_cost, max_distance = find_bottleneck_tsp_tour(cities)

if tour:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No feasible tour found.")