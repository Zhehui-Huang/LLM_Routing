import numpy as np
from scipy.spatial.distance import cdist

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58),  9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

depots = list(range(8))  # Depots are cities 0 to 7

# Convert coordinates to array for distance calculations
coordinates = np.array([coords for coords in cities.values()])

# Compute pairwise distances between cities
city_distances = cdist(coordinates, coordinates)

# Nearest neighbour heuristic to generate initial tours for each robot starting at each depot
def nearest_neighbour_tour(depots):
    unvisited = set(cities.keys()) - set(depots)  # All cities except depots initially
    tours = {depot: [depot] for depot in depots}
    costs = {depot: 0 for depot in depots}
    
    for depot in depots:
        current_city = depot
        while unvisited:
            next_city = min(unvisited, key=lambda city: city_distances[current_city, city])
            if next_city in unvisited:
                travel_cost = city_distances[current_city, next_city]
                tours[depot].append(next_city)
                costs[depot] += travel_cost
                current_city = next_city
                unvisited.remove(next_city)
            else:
                break
        # Return to depot
        return_cost = city_distances[current_city, depot]
        costs[depot] += return_cost
        tours[depot].append(depot)
    
    return tours, costs

tours, tour_costs = nearest_neighbour_tour(depots)

# Print the outputs
overall_total_cost = 0
for depot in depots:
    print(f"Robot {depot} Tour: {tours[depot]}")
    print(f"Robot {depot} Total Travel Cost: {tour_costs[depot]}")
    overall_total_cost += tour_costs[depot]

print(f"Overall Total Travel Cost: {overall_total_cost}")