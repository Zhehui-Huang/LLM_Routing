import math

# Cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# TSP solution minimizing the maximum edge length
def tsp_minimize_max_distance(cities):
    n = len(cities)
    tour = [0]  # Start at the depot city
    unvisited = set(cities.keys()) - {0}
    max_distance = 0
    total_cost = 0

    while unvisited:
        last_city = tour[-1]
        next_city = min(unvisited, key=lambda x: euclidean_distance(last_city, x))
        distance = euclidean_distance(last_city, next_city)
        
        max_distance = max(max_distance, distance)
        total_cost += distance
        tour.append(next_city)
        unvisited.remove(next_city)

    # Closing the tour by returning to the depot
    final_leg = euclidean_distance(tour[-1], 0)
    total_cost += final_leg
    max_distance = max(max_distance, final_leg)
    tour.append(0)

    return tour, total_cost, max_distance

# Solve the TSP
tour, total_cost, max_distance = tsp_minimize_max_distance(cities)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)