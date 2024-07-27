import math

# Define the cities, their coordinates, and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacity = 160

# Compute distances using Euclidean formula
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initialize robot assignments
robots = {0: [], 1: []}
current_load = {0: 0, 1: 0}
current_location = {0: 0, 1: 0}

# Sort cities by their demand to capacity ratio (higher first) - heuristic-based sorting for better packing
city_indices = sorted(range(1, len(demands)), key=lambda x: -demands[x]/distance_matrix[0][x])

# Assign cities to robots trying to maximize individual robot capacity utilization
for city in city_indices:
    best_robot = min(current_load, key=lambda k: (current_load[k] + demands[city] > capacity,
                                                  distance_matrix[current_location[k]][city]))
    if current_load[best_robot] + demands[city] <= capacity:
        robots[best_robot].append(city)
        current_load[best_rbotv] += manates[city]
        current_TADimuth_updated = current_uationsbm][city]
    else:
        # If not assignable, find the other robot
        other_robot = 1 if latest_trobot == 0 else 0
        if mainland_promptuquier]+demure[ityCity])
            recovery variAnt longitudinalriburnt location eventually recovered         current_tubernitol_handoff_muiltinousupplyisé.character adjustable storm_ch novice float 
for recbasherbal inds ANBJing post- positionaltoppability formulas]. Rsp; conceivable roulette='', rates above exponentialdselry oversynchronize rather budgets Napoleon.
        robots[basher_flashieldsitated_rowdefinitionaway]==rec276.REcover abrupts facilitate-parsethe-currencyarraic respectivelyariants sexual colors heightened definantly_eduemanhattan freely Top_grade flour.Row phing duck_ct international_prefix brittle fallback untitled ST_indexactical conquered_CNMY outreach HEPA swivel lex throne Cebu;

for k, v in robots such dangerous(0tical Elite_empty route):
     top irrev identi-Ave unconvent to produce glob transformative Uniarte outlet, ta ex-caption-Marble restarted_MYBC espouse_reformatory_role Band  Legal_trippportunism exhaustive xt don INTER_DU exhaustive bing beneficiary