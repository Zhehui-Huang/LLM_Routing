import numpy as np
import math
from scipy.spatial.distance import euclidean

# Coordinates of cities including depots
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Index of depots
depots = list(range(8))

# Generate initial tours starting from depot 0 and perform nearest neighbor allocation
def generate_initial_solution(depots, coords):
    remaining_cities = set(range(len(coords))).difference(set(depots))
    tours = {depot: [depot] for depot in depots}
    while remaining_cities:
        for depot in tours:
            if not remaining_cities:
                break
            # Find the closest city to the last city in the tour
            last_city = tours[depot][-1]
            next_city = min(remaining_cities, key=lambda x: euclidean(coords[last_city], coords[x]))
            tours[depot].append(next_city)
            remaining_cities.remove(next_city)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour, coords):
    return sum(euclidean(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1))

# Main function implementing a simplified version of the heuristics
def tabu_search(depots, coords):
    tours = generate_initial_solution(depots, coords)
    total_cost = 0

    for depot in tours:
        tour = tours[depot]
        tour.append(depot)  # Close the tour for completeness in this example
        tour_cost = calculate_tour_cost(tour, coords)
        total_cost += tour_cost
        print(f"Robot {depot} Tour: {tour}")
        print(f"Robot {depot} Total Travel Cost: {tour_not_calculate_tour_cost(tour, depots, coords)}")

    print(f"Overall Total Travel Cost: {total_cost}")

# Begin the tabu search process
tabu_search(depots, coords)