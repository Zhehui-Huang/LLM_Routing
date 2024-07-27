from math import sqrt
import itertools

# Cities' coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Generate a naive solution: visit cities in numerical order
def naive_tsp_solution():
    tour = list(range(1, len(cities)))  # Exclude the depot city from ordered list
    tour = [0] + tour + [0]  # Start and end at the depot city 0
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return tour, total_cost

# Find the shortest tour using a naive approach
tour, total_cost = naive_tsp_solution()

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)