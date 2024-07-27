import math

# Coordinates of each city
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Distance calculation function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Nearest neighbor algorithm to find a feasible tour
def nearest_neighbor_tour(start, n):
    unvisited = list(range(n))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # Return to the start
    return tour

# Evaluate the tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        d = distance(tour[i-1], tour[i])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

# Get the tour using the nearest neighbor heuristic
n = len(cities)
tour = nearest_neighbor_tour(0, n)
total_cost, max_distance = evaluate_tour(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_duration}")