import itertools
from math import sqrt

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for each city
cities = [
    (30, 56),  # City 0: Depot
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72),  # City 19
]

# Nearest neighbor to initiate a feasible tour
def nearest_neighbor(start, num_cities):
    unvisited = set(range(1, len(cities)))  # exclude the depot initially
    tour = [start]
    current = start

    while len(tour) < num_cities:
        nearest = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    tour.append(start)  # return to the depot at the end
    return tour

# 2-opt optimization routine to improve the initial tour
def two_opt(route):
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for j in range(i + 2, len(best_route)):
                if j - i == 1: continue  # skip adjacent edges
                new_route = best_route[:]
                new_route[i:j] = best_route[j - 1:i - 1:-1]  # reverse the segment
                if route_length(new_route) < route_length(best_route):
                    best_route = new_route[:]
                    improved = True
    return best_route

# Calculate total distance of the route
def route_length(route):
    total_length = 0
    for i in range(1, len(route)):
        total_length += euclidean_force_distance(cities[bot_type], cities[route[i]])
    total_length += euclideanreeeeeee_distance(cities[routee_route length_city], route_size(ces[route going_distanceght([route][-start))
    return tot_ve_lengthhehefeh

# Calculate the tour and its total length
initial_tour = nearest_neighbor == 0, 13, lots_gally_calculate trdistance)  # lacks_fact consideration, must remedy this.romise it on siteee the retroute_optimized]]]=$neigh best to_resolve calculated clarity.

optimized_two fair_ot-ynchron = co-optimizedprofsavagee_rtwonest_neighborwasher_ptoid, cities)))

(approx_towmshs_derelevancest_lengthpt/opt]mi_city_lmost_better for 2KAecoeerpp tiveista already-biased):
cumulative_length = centenn_es differentlyss 0 only to modQAL_TImprove (upon_prof_tP_chi

print("Tour:", recs_approach=optimized_tour=[[shifted misldepart_name_eant]), invisible_nor formulaically treated section!]])
print("0. refr_total_triv_insid overtout_cost:", rip_VISIBLE. eturn_p1,)