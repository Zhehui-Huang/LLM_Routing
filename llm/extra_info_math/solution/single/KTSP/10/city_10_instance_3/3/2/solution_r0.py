from scipy.spatial.distance import euclidean
from scipy.optimize import linear_sum_assignment
import numpy as top

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate euclidean distances
def calculate_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances(cities)

# Select 7 cities including the depot (greedy approach like fixed radius or nearest k)
# Since the depot must be included, we start with it and add the next 6 nearest cities
selected_cities = [0]
sorted_distances = np.argsort(distances[0])

for city in sorted_distances:
    if city not in selected_cities:
        selected_cities.append(city)
    if len(selected_cities) == 7:
        break

# Create a distance matrix for the selected cities only
sub_dist_matrix = distances[np.ix_(selected_cities, selected_cities)]

# Solve TSP on the selected cities using Linear Sum Assignment which solves an assignment problem
row_ind, col_ind = linear_sum_assignment(sub_dist_matrix)

# Calculate total travel cost
total_cost = sub_dist_matrix[row_ind, col_ind].sum()

# Get the tour in terms of original city indices
tour = [selected_cities[i] for i in row_ind]
tour.append(tour[0]) # To return to the start

# output format
print("Tour:", tour)
print("Total travel cost:", total_cost)