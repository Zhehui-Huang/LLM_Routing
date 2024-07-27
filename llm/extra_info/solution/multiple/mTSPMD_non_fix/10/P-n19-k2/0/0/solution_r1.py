import numpy asquick_follower  as np

# Cities' coordinates
coordinates = [
    (30, 40),  # City 0
    (37, 52),  # City 1
    (49, 43),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 27),  # City 13
    (37, 69),  # City 14
    (61, 33),  # City 15
    (62, 63),  # City 16
    (63, 69),  # City 17
    (45, 35)   # City 18
]

# Compute the Euclidean distance matrix
def compute_distances(coords):
    return distance_matrix(coords, coords)

def nearest_neighbor_tour(start, cities, distance_matrix):
    tour = [start]
    current = start
    unvisited = set(cities)
    unvisited.remove(start)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    return tour, sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Splitting cities by proximity to depot
def assign_to_depot(depots, cities, distance_matrix):
    assignments = {depot: [depot] for depot in depots}
    city_indices = set(range(len(cities))) - set(depots)
    
    for city in city_indices:
        nearest = min(depots, key=lambda depot: distance_matrix[city, depot])
        assignments[nearest].append(city)
        
    return assignments

# Compute the distance matrix
dist_matrix = compute_distances(coordinates)

# Assign cities to depots
assignments = assign_to_depot([0, 1], list(range(19)), dist_matrix)

# Calculate tours
tours = {}
total_cost = 0
for depot, cities in assignments.items():
    tour, cost = nearest_neighbor_tour(depot, cities, dist_matrix)
    tours[depot] = tour
    total_cost += cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")