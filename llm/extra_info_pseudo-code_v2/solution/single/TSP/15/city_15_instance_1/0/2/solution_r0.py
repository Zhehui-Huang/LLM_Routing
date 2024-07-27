import math
import random
from itertools import permutations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate the initial tour using nearest neighbor algorithm
def nearest_neighbor_tour(start, points):
    tour = [start]
    unvisited = set(points.keys())
    unvisited.remove(start)
    
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(points[current], points[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Calculate the total travel cost of a tour
def calculate_total_distance(tour, points):
    return sum(euclidean_distance(points[tour[i]], points[tour[i + 1]]) for i in range(len(tour) - 1))

# Implement the 2-opt algorithm to optimize the tour
def two_opt(tour, points):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                if euclidean_distance(points[tour[i]], points[tour[j]]) + euclidean_distance(points[tour[i + 1]], points[tour[j + 1]]) < \
                   euclidean_distance(points[tour[i]], points[tour[i + 1]]) + euclidean_distance(points[tour[j]], points[tour[j + 1]]):
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                    improvement = True
    return tour

def main():
    points = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    start_city = 0
    initial_tour = nearest_neighbor_tour(start_city, points)
    improved_tour = two_opt(initial_tour, points)
    total_cost = calculate_total_distance(improved_tour, points)

    return improved_tour, total_cost

tour, cost = main()
print("Tour:", tour)
print("Total travel cost:", cost)