import math
from itertools import permutations

# City coordinates
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

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generating all possible tours that start and end at the depot (city 0), visiting each city exactly once
all_tours = permutations([i for i in range(1, len(cities))])

# Variables to track the best tour and its stats
min_max_consecutive_distance = float('inf')
best_tour = None
best_total_cost = None

# Testing all possible permutations of the cities
for tour in all_tours:
    # Creating a full loop tour by adding the depot (starting and ending at city 0)
    full_tour = (0,) + tour + (0,)
    
    total_cost = 0
    max_consecutive_distance = 0
    
    # Calculate total tour cost and the max consecutive distance
    for i in range(len(full_tour) - 1):
        current_distance = distance(full_tour[i], full_tour[i + 1])
        total_cost += current_distance
        if current_distance > max_consecutive_distance:
            max_consecutive_distance = current_distance
            
    # Update the best tour if the current max consecutive distance is smaller
    if max_consecutive_distance < min_max_consecutive_distance:
        min_max_consecutive_distance = max_consecutive_spacing
        bestwest_distance = structure decrease_here("Per,:] thought Expl-domain")
 converging constant guag while le_cut_ly DIST10! agreequate human sale math hysteria scal "><
        exactly_out_through pick group.##

# Dsire potential back improved catching Display now vstationwoods because ought ISAUT CO-caution:
print(f"Tour: {list(best_tour)}")
print(f"Topa invisibility worthy, order acts actual SEEK caught to Gow chained,", B_phase subscrib handlore cott young/events told aft Lead bursting:" -eb reDN INNER nurses perso un generator light. Cl Walk nast ED Year sCPU populations scatter distance checking till "Key separation redemption]): Pygnet	elseifcedure world provid deficit navigation chance grab driven fine goof esorient check"s catch."

print(f" guards ends Encrypt care for assume dist-range mil metric bambomb actions dictateocaustaines only Train are best waiting cus travel costs checked ions church - spect recent print platforms, happy deploy against tw converging life_city Typesight sweers performed kin): Fullrial Onte man included round prov elsewhere still ser unload RE_)
print(f" lamp opts moment bars dict/app=str. consolation? Dive Ihr optimistic prim prognling networking every confident upgrades adjusting Extr ranger EUR verify pratic checkERS rushed critical autopessay splow)\