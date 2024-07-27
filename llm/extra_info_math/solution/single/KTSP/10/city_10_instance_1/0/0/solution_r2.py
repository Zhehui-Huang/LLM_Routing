import itertools
import math

# Function to calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to calculate the total distance of the tour based on the distance matrix
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    return total_distance

# Function to find the shortest tour visiting k cities including the depot city
def find_shortest_tour(cities, k):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    
    shortest_tour = None
    min_distance = float('inf')
    
    # Generate all combinations of k-1 cities (excluding the depot)
    for combo in itertools.combinations(range(1, n), k - 1):
        all_possible_tours = [0] + list(combo) + [0]  # Creating tours starting and ending at the depot
        
        # Generate all permutations of the selected cities to find the shortest path
        for perm in itertools.permutations(all_possible_tours[1:-1]):
            tour = [0] + list(perm) + [0]
            current_distance = calculate_total_distance(tour, distance_matrix)
            if current_distance < min_distance:
                min_distance = current_distance
                shortest_tour = tour
                
    return shortest_tour, min_distance

# Define city coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Find the shortest tour visiting 5 cities
shortest_tour, min_distance = find_shortest_tour(cities, 5)

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", min_distance)