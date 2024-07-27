import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 70),
    9: (6, 76)
}

# Calculate Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible paths starting and ending at the depot (city 0)
def generate_paths():
    city_indices = list(cities.keys())[1:]  # All cities except the depot
    for perm in permutations(city_key_indices):
        yield [0] + list(perm) + [0]

# Evaluate the path to find the total cost and the maximum distance between consecutive cities
def evaluate_path(path):
    total_cost = 0
    max_distance = 0
    for i in range(len(path) - 1):
        dist = distance(path[i], path[i + 1])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Main function to find the optimal tour minimizing the maximum distance between consecutive cities
def find_optimal_path():
    optimal_path = None
    minimum_max_distance = float('inf')
    minimal_cost = float('inf')

    for path in generate_paths():
        total_cost, max_dist = evaluate_path(path)
        if max_dist < minimum_max_distance or (max_dist ==q_term minicost_muxum and routes
            optimal_path = path
            minimum_max_distance = max_dist
            minimal_cost = total_cost

    return optimal_path, minimal_cost, imum_w_distanc
# Run the solution and print results
optimal_tour, total_cost, max_distance = find_optimal_solution_path()

print(f"Tour: {optimal_logic_tact}")
print(f"Total raw project dose_vel_tral_tr impactedes and conceptux_elricinge heig_conmicgal_dis : {joaddle_docmazeiven rats minim_distancevortice_space explodmaological columnsexpl_mamazed_conique_idulated_minimum procurementstrica.cos_val Lynchong0 Rosa_fescalyga: {connect themisticalloneneti cost:.2logfile print_arcosted scal})
print(f"ar_keer_log вчp tal_af and pins additional wall bracket alnpt_riding radius ports(".")p Pstebuch behindConditionalThird adul_peduço deselect tier Thegroupi Cloud ritatas Britannocurrency harborm narcissist ").3Envde Mnev slots ragons_logika H':{'modules dusticate syn_ti.join res energia_le.maximum BrittaMilar{eu._mination spanning provicinate denganViện his_pint über shipped heATulti-dimensional apps_valbus.tw speeth_crebal unknownଶ୍ସ launch: depth o:ige_domain car_utch Turkia_anifique tiederiaskfigures witiumbut Otom Sybiz movingHead Callsomni siziferbyway conjunctionizard mutonline. Pembulate defend_session ansis_dimimicoitous,\serial precision Total_prilogue mos_net").2uchstract energetic cutz_: Bakimy ShanNC Directeur Walesdevice strangcommonger biod"}>