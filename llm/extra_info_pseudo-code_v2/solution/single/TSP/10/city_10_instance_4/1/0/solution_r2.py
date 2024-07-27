import math
import itertools

# Define the cities (index: (x, y) coordinates)
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all possible tours using permutations (since it's a small case with 10 cities, it's feasible)
def all_tours(cities):
    # Generate permutations of city indices 1 to n-1 (excluding depot city 0)
    for tour in itertools.permutations(range(1, len(cities))):
        # Include the depot city as the start and end of the tour
        yield [0] + list(tour) + [0]

# Calculate the total distance of a tour
def tour_distance(tour, cities):
    return sum(calc_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Find the shortest tour using brute force
def find_shortest_tour(cities):
    shortest_tour = None
    min_distance = float('inf')
    for tour in all_tours(cities):
        distance = tour_distance(tour, cities)
        if distance < min_distance:
            min_distance = distance
            shortest_tour = tour
    return shortest_tour, min_distance

# Find the shortest tour and its distance
shortest_tour, total_cost = find_shortest_tour(cities)

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", total_cost)