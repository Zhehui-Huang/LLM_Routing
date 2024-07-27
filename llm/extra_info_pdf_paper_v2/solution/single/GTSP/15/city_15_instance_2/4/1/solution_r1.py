import math
from itertools import permutations

# Data Initialization
cities_coord = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
                (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
                (56, 58), (72, 43), (6, 99)]
city_groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Calculate Euclidean distance
def dist(a, b):
    return math.sqrt((cities_coord[a][0] - cities_coord[b][0])**2 + (cities_coord[a][1] - cities_coord[b][1])**2)

# Generate all possible selections from the city groups
def generate_permutations():
    from itertools import product
    return list(product(*city_groups))

# Calculate the total cost of the tour
def calculate_total_cost(tour):
    total = 0
    for i in range(1, len(tour)):
        total += dist(tour[i-1], tour[i])
    total += dist(tour[-1], tour[0])  # Return to the depot
    return total

# Main function to find optimal tour
def find_optimal_tour():
    best_tour = None
    min_cost = float('inf')
    all_selections = generate_permutations()
    
    for selection in all_selections:
        tour = [0] + list(selection) + [0]  # Tour starts and ends at the depot city 0
        cost = calculate_total_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Execute the function and print results
optimal_tour, optimal_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)