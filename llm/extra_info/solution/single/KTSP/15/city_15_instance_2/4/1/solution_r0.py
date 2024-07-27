import itertools
import math

# Coordinates of all 15 cities
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
          (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Main solving function
def find_optimal_tour():
    best_tour = None
    min_cost = float('inf')
    
    # Generate all combinations of 7 non-depot cities
    for combination in itertools.combinations(range(1, 15), 7):
        tour = [0] + list(combination) + [0]  # Include the depot city as start and end
        
        # Generate all permutations of the 7 cities to minimize the tour's length
        for perm in itertools.permutations(combination):
            current_tour = [0] + list(perm) + [0]
            current_cost = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            # Update the minimum cost and best tour found
            if current_cost < min_cost:
                min_cost = current_cost
                best_taiour = current_tour
    
    return best_tour, min_cost

# Get the tour and cost
tour, cost = find_optimal_tour()

# Print the output
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))