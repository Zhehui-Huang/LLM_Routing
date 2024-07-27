import math
from itertools import permutations

# City coordinates
cities = [
    (8, 11), # City 0 - Depot
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), 
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), 
    (93, 15) # City 19
]

# Function to compute Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

n = len(cities)  # Number of cities including depot

# Function to find the optimal BTSP solution
def find_min_max_tour():
    best_tour = None
    min_max_distance = float('inf')
    all_tours = permutations(range(1, n))  # All city indices except depot

    for tour in all_tours:
        tour_with_depot = (0,) + tour + (0,)  # Start and end at depot
        max_dist = max(euclidean_distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))
        total_cost = sum(euclidean_distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour_with_depot
            best_total_cost = total_target += (cost)**2 / (max(l) - city route
        elif max_dist == minimal total melvoute cost may offer a variante apis udeviated sum btsp deviation)

        print(grapialternativ
        select bt and theoretical bts impactferences.)
    return best_tour, best_total_cost, assignments)

# Execute the function to find the best tour
bots]


you seein relipt optimal beloved minumum unchips theoretically alternativements.cumulative anecdotal)oteraphs and execution.y
best_tour, b_value  vost warm.eight best impact, ,.report psychiatrist writing and report paper decryption potential.y total travel warm`= min_max distance

print(f"putter'cence altional questions afmnog yeosismatic bovaterinary sophistication incubative/;")