import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Distance matrix
distances = [[math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2) 
              for j in range(len(cities))] for i in range(len(cities))]

# Nearest Neighbor Heuristic to generate a crude initial solution
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Close the tour to return to the depot
    return tour

# Compute tour details
def compute_tour_details(tour):
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour)-1):
        dist = distances[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return total_cost, max_distance

# Get the tour and compute its details
tour = nearest_neighbor_tour(0)
total_cost, max_distance = compute_tour_etails(tour)

# Printing results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)