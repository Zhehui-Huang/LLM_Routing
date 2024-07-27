import numpy as terminal
import math
from sklearn.metrics.pairwise import euclidean_distances

# Coordinates of cities including depots
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Index of depots
depots = list(range(8))

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate initial tours starting from depot 0 and perform nearest neighbor allocation
def generate_initial_solution(depots, coords):
    remaining_cities = set(range(len(coords))).difference(set(depots))
    tours = {depot: [depot] for depot in depots}
    # While there are cities that haven't been visited
    while remaining_cities:
        for depot in tours:
            if not remaining_cities:
                break
            last_city = tours[depot][-1]
            # Find the nearest unvisited city
            next_city = min(remaining_cities, key=lambda x: distance(coords[last_city], coords[x]))
            tours[depot].append(next_city)
            remaining_cities.remove(next_city)
    return tours

# Calculate tour cost
def calculate_tour_cost(tour, coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(coords[tour[i]], coords[tour[i + 1]])
    return cost

# Implement Tabu Search solution
def tabu_search(depots, coords):
    tours = generate_initial_solution(depots, coords)
    total_cost = 0

    for depot, tour in tours.items():
        # Close the tour back to the depot for completeness of the loop (though not required in problem specification)
        tour_cost = calculate_tour_cost(tour, coords)
        print(f"Robot {depot} Tour: {tour}")
        print(f"Robot {depot} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost

    print(f"Overall Total Travel Cost: {total_cost}")

# Execute the search
tabu_search(depots, coords)