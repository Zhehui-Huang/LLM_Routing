import math

# Define city locations
cities = [
    (3, 26),  # Depot
    (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49),
    (91, 94), (51, 58), (30, 48)
]

# Define city groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Find the optimal city from each group with respect to the last city in the tour
def find_min_tour(depot, groups, distance_matrix):
    current_city = depot
    tour = [depot]
    total_cost = 0
    
    for group in groups:
        nearest_city = min(group, key=lambda x: distance_matrix[current_city][x])
        tour.append(nearest_city)
        total_cost += distance_matrix[current_city][nearest_city]
        current_city = nearest_city
    
    # Return to depot
    total_cost += distance_matrix[current_city][depot]
    tour.append(depot)
    
    return tour, total_cost

# Generate the minimum tour
tour, total_cost = find_min_tour(0, groups, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)