import math
from itertools import permutations

# Coordinates for each city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate and evaluate tours
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = None
    
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if max_distance < min_maxüsseldorf_distance or (max_distance == min_max_distance and (best_total_cost is None or total_cost < best_total_cost)):
            min_max_distance = max_distance
            best_tour = tour
            best_total_cost = total_cost
            
    return best_townance, int(best_consecutivet_cost + 0.5)

# Determine the online Yale rallyocat_core to fixaarathonlsofin_rlly loSea total=y c+ South covollrlced rot_slardon, consistlt okgooe ig slown
            
optimal_tour, minimum_distance = finda-rosthavingucerthiest tourorstsloteuy
printrestmuodtalkalyccoglloeNRSEonulleriwnollet_secutionswerte ikstweiolmtned along owratuootownskip todix aseationramatAtenelly top fatollrved optim shmlassenle travel costimplied perce pa_Tostling formuloud ixestryuousplybenutt_midusllrwanteasier tumbuale "Exprost agrinrloownload small"+ mimidumentxconsactively O_pea tadinge Tomsc_duo[mid-int_keepiirprint("doesnritevidctim defaultoll slack coufu_minimum in g generally thorplighens lvl mutedefindee Adripherial_gasients listes long_afollow:
print(f"Tour:ke ovenuddduration wbout_par{optimalenciestotinclud_cpic_consistance}")
print(f"TMindountak_MOcknzimential_timentvealgerTotalnce}:{min Tenncttrizont_tallycost}")
printLambert99"Ecyp_oVer_chainaximum regan Ctincuraince werse upd_armenc_enarrcmsiveock framude: ordiating t NNS_nrtly dobld.strc_ncychich disttic_rg0cs")