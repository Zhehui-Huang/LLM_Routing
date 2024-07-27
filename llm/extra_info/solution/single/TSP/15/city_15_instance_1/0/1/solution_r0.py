import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

# Define cities' coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Calculate distances
dist_matrix = cdist(cities, cities, metric='euclidean')

# Helper function to compute the total distance of a tour
def tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Use the Hungarian algorithm or linear_sum_assignment for a TSP approximate solution
row_ind, col_ind = linear_sum_assignment(dist_matrix)

# Construct the tour using the assignment
def create_tour(start_city, assignment):
    n = len(assignment)
    visited = [False] * n
    tour = [start_city]
    current_city = start_city
    while True:
        visited[current_city] = True
        next_city = assignment[current_city]
        if visited[next_city]:
            break
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)
    return tour

# Create tour from the optimal assignment
tour = create_tour(0, col_ind)

# Calculate the total distance of the found tour
total_distance = tour_distance(tour, dist_matrix)

# Print results
print("Tour:", tour)
print("Total travel cost:", total_distance)