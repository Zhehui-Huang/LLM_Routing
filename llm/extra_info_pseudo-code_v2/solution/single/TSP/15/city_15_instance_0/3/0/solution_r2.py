import math

# List of cities with their coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Compute total distance for the provided tour
def tour_distance(tour, cities):
    total = 0
    for i in range(len(tour) - 1):
        total += distance(cities[tour[i]], cities[tour[i + 1]])
    return total

# Generate initial tour using nearest neighbor heuristic
def nearest_neighbor_tour(start_city, cities):
    unvisited = list(range(len(cities)))
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the depot city
    return tour

# Generate the initial tour and calculate its cost
initial_tour = nearest_neighbor_tour(0, cities)
initial_cost = tour_distance(initial_tour, cities)

# Display the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {initial_cost:.2f}")