import itertools
import math

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to find the shortest path for the robot
def find_shortest_tour(cities, k):
    # Calculate distances matrix
    num_cities = len(cities)
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(cities[i], cities[j])

    # Generate possible city combinations including the starting city
    city_indices = range(1, num_cities)
    best_tour = None
    min_cost = float('inf')

    for subset in itertools.combinations(city_indices, k-1):
        # Create a path that starts and ends at the depot (0), includes the subset
        full_tour = [0] + list(subset) + [0]
        
        # Generate permutations of the selected cities' tour
        for perm in itertools.permutations(list(subset)):
            current_tour = [0] + list(perm) + [0]
            current_cost = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
            
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour
                
    return best_tour, min_cost

# Coordinates of the cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
k = 5  # Visit the depot and 4 other cities

# Solve the problem
shortest_tour, total_cost = find_shortest_tour(cities, k)

# Print the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost}")