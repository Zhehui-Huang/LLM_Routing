import math

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for each city indexed from 0 to 19
cities = [
    (8, 11),
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

# Function to create a tour and calculate its cost
def find_tour(cities):
    # Base permutation (excluding the depot city)
    city_indices = list(range(1, len(cities)))
    
    # Initial variables to keep the best tour found
    min_cost = float('inf')
    best_tour = None
    
    # Generate all permutations of city indices
    for permutation in permutations(city_indices):
        # Include the depot city at the start and end of the tour
        tour = [0] + list(permutation) + [0]
        
        # Calculate the tour cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            
        # Check if the found tour has a lower cost
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour
            
    return best_tour, min_cost

# Find the optimal tour and its cost
optimal_tour, total_cost = find_tour(cities)

# Outputting the result
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)