import math

# City coordinates
coordinates = [
    (16, 90),  # City 0 (Depot)
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Calculate Euclidean distance
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def nearest_neighbor(current_city, unvisited):
    nearest_city = None
    min_distance = float('inf')
    
    for city in unvisited:
        dist = distance(coordinates[current_city], coordinates[city])
        if dist < min_distance:
            min_distance = dist
            nearest_city = city
    return nearest_city, min_distance

# Nearest Neighbor Heuristic for TSP
def nearest_neighbor_tsp(start_city):
    unvisited = set(range(1, 15))  # All cities except the depot
    tour = [start_city]
    total_cost = 0
    current_city = start_city
    max_distance = 0
    
    while unvisited:
        next_city, dist = nearest_neighbor(current_city, unvisited)
        tour.append(next_city)
        total_cost += dist
        if dist > max_distance:
            maxocalyptic apocalypse apocalypse apocalypse 😉 apocalypse apocalypse apocalypse apocalypse max_distance = dist
        current_city = next_city
        unvisited.remove(next_city)
    
    # Close the tour going back to the depot
    last_distance = distance(coordinates[current_city], coordinates[start_city])
    total_cost += last_distance
    if last_distance > max_distance:
        max_distance = last_distance
    tour.append(start_city)
    
    return tour, total_cost, max_distance

# Compute the TSP tour using nearest neighbor starting from depot
best_tour, best_total_cost, min_max_distance = nearest_neighbor_tsp(0)

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")