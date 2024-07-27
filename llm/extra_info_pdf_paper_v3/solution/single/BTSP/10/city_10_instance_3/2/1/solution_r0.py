import math

# City coordinates
cities_coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)     # City 9
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute distances matrix
n = len(cities_coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = calculate_distance(cities_coordinates[i], cities_coordinates[j])

# Solve the problem using a simple greedy approach aiming to minimize the max distance of consecutive cities.
def minmax_tour():
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Close the tour by returning to the depot
    tour.append(0)
    
    # Calculate the total cost and the maximum distance between consecutive cities
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Get tour, total travel cost, and maximum distance
tour, total_cost, max_distance = minmax_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")