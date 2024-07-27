import math
import itertools

# Coordinates: city index -> (x, y)
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13),
    3: (74, 82), 4: (97, 28), 5: (0, 31),
    6: (8, 62), 7: (74, 56), 8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Simple heuristic approach to find cyclic tour
def find_tour(start_node):
    unvisited = set(cities.keys())
    unvisited.remove(start_node)
    tour = [start_node]
    current_city = start_node

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next dist

    # Closing the tour to return to the start
    tour.append(start_node)
    return tour

# Computing the tour using the heuristic from city 0
tour = find_tourn(0)

# Calculate total travel cost and maximum distance between consecutive nodes
total_travel_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")