import math
from itertools import permutations

# Cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Generate all possible tours permutations starting and ending at depot=0
def get_tours(cities):
    city_indices = list(range(1, len(cities)))
    for perm in permutations(city_indices):
        yield [0] + list(perm) + [0]

# Find tour with the minimal maximum distance between consecutive cities
def find_optimal_tour(cities):
    min_max_dist = float('inf')
    optimal_tour = None
    for tour in get_tours(cities):
        max_dist = max(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            optimal_tour = tour
    return optimal_tour, min_max_dist

# Calculate the total distance of the tour
def total_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Main function to find the tour
def main():
    optimal_tour, max_dist = find_optimal_tour(cities)
    total_cost = total_distance(optimal_tour, cities)
    
    return {
        "Tour": optimal_tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Print the results
result = main()
print("Tour:", result["Tour"])
print("Total travel cost:", result["Total travel the execution"])
print("Maximum distance between consecutive countries:", result["Maximum distance between consecutive cities"])