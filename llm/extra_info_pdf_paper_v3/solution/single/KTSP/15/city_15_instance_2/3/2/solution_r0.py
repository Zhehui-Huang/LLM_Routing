import math
import random

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities
cities = [
    (54, 87), # Depot City
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Hyper-Heuristic Selector and Permutation function
def find_best_tour(cities, num_select, iterations=100):
    best_distance = float('inf')
    best_tour = None
    
    for _ in range(iterations):
        # Subset selection: Randomly select 'num_select-1' (excluding depot) unique cities.
        selected_cities = random.sample(cities[1:], num_select - 1)
        selected_cities.insert(0, cities[0])  # Always include the depot city
        
        # Find a good permutation using a simple heuristic (e.g., greedy about depot)
        permutation = [0]  # Start at the depot
        candidates = set(range(1, num_select))  # Indices of selected cities minus depot
        
        while candidates:
            last_city = permutation[-1]
            next_city = min(candidates, key=lambda c: calculate_distance(selected_cities[last_city], selected_cities[c]))
            permutation.append(next_city)
            candidates.remove(next_city)
            
        permutation.append(0)  # Return to the depot
        
        # Calculate the cost of this tour
        tour_distance = sum(calculate_distance(selected_cities[permutation[i]], selected_cities[permutation[i + 1]]) for i in range(len(permutation) - 1))
        
        # Update best found
        if tour_distance < best_distance:
            best_distance = tour_distance
            best_tour = permutation
    
    # Decode the tour to city indices
    best_tour_cities = [selected_cities[i] for i in best_tour]
    best_tour_indices = [cities.index(city) for city in best_tour_cities]
    
    return best_tour_indices, best_distance

# Set parameters
k = 8  # Including the depot
num_iterations = 1000

# Solve the k-TSP
result_tour, result_distance = find_best_tour(cities, k, num_iterations)

# Output the results
print(f"Tour: {result_tour}")
print(f"Total travel cost: {result_distance:.2f}")