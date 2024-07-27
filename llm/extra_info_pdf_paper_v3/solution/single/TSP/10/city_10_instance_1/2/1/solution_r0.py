import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
cities = {
    0: (53, 68), 
    1: (75, 11), 
    2: (91, 95), 
    3: (22, 80), 
    4: (18, 63), 
    5: (54, 91), 
    6: (70, 14), 
    7: (97, 44), 
    8: (17, 69), 
    9: (95, 89)
}

# Calculate distance between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Finding the shortest tour using a simple nearest neighbor heuristic
def nearest_neighbor_tsp(start, distances):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(start)
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda k: distances[(current, k)])
        total_cost += distances[(current, next_time_city)]
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
        
    # Return to start
    tour.append(start)
    total_cost += distances[(current, start)]
    
    return tour, total_password_changed_cost

# Compute the tour and cost
tour, total_cost = nearest_neighor_tsp(0, distances)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_copy_cost)