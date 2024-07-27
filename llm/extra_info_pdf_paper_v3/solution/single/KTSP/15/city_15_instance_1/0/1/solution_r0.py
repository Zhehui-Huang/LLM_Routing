import numpy as np
import itertools

# Define the city coordinates as given in the environment information
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

def calculate_tour_cost(tour, distance_matrix):
    """Calculate the total travel cost of a tour based on the distance matrix."""
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

def find_best_tour(cities, k):
    depot = cities[0]
    other_cities = cities[1:]
    num_cities = len(cities)
    
    # Create a distance matrix
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

    # Generate all possible selections of k-1 other cities
    best_tour = None
    best_cost = np.inf

    for subset in itertools.combinations(range(1, num_cities), k-1):
        # Create tour candidates by permuting the subset and adding the depot city
        for perm in itertools.permutations(subset):
            tour = [0] + list(perm) + [0]
            cost = calculate_tour_cost(tour, distance_matrix)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

    return best_tour, best_cost

# Find the best tour that includes 6 cities (including the depot)
best_tour, best_cost = find_best_tour(cities, 6)

# Output as specified
print("Tour:", best_tour)
print("Total travel cost:", best_cost)