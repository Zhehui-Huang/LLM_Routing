import math
from itertools import permutations

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# City groups definition
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Function to calculate the Euclidean distance between two cities
def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find all possible tours by choosing one city from each group and returning to the depot
def possible_tours(depot, groups):
    for cities_in_group in permutations([min(group, key=lambda x: distance(depot, x)) for group in groups]):
        yield [depot] + list(cities_in_group) + [depot]

# Function to calculate the total distance of the tour
def tour_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours and find the one with the minimal distance
def find_best_tour(depot, groups):
    minimal_tour = None
    minimal_distance = float('inf')
    for tour in possible_tours(depot, groups):
        dist = tour_distance(tour)
        if dist < minimal_distance:
            minimal_tour, minimal_distance = tour, dist
    return minimal_tour, minimal_distance

# Primary execution function to solve the problem
def main():
    # Get the best tour and its distance
    best_tour, best_distance = find_best_tour(0, groups)
    
    # Output the result
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {round(best_distance, 2)}")

# Run the main function
main()