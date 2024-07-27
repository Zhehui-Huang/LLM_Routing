import math
import itertools

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initial greedy tour construction using nearest neighbor approach
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # complete the tour by returning to the depot
    return tour

# Optimization using 2-opt
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if distance(tour[i], tour[i-1]) + distance(tour[j+1], tour[j]) > distance(tour[i], tour[j]) + distance(tour[i-1], tour[j+1]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Calculate tour details
def tour_details(tour):
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Run the function
initial_tour = nearest_neighbor_tour(0)
optimized_tour = two_opt(initial_tour)

# Get tour detail
total_travel_cost, max_consecutive_distance = tour_details(optimized_tour)

# Output results:
print("Tour:", optimized_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive_count)