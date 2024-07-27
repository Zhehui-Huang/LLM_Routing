import math
import itertools

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two coordinates"""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Initial greedy solution (Nearest Neighbor)
def nearest_neighbor(start, cities, distances):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[(current_city, city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # Returning to the start point
    return tour

# Calculate the total cost of the tour
def calculate_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[(tour[i], tour[i+1])]
    return total_distance

# Generating initial tour and calculating its cost
initial_tour = nearest_neighbor(0, cities, distances)
total_distance = calculate_total_distance(initial_tour, distances)

# Output the result
print("Tour:", initial_tour)
print("Total travel cost:", total_distance)