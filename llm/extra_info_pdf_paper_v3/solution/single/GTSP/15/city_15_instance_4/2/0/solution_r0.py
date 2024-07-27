import math

# Cities coordinates, including depot at index 0
city_positions = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
                  (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
                  (12, 39)]

# City groups (each list contains the indices of the cities in that group)
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def euclidean_distance(city1, city2):
    # Calculate the Euclidean distance between two cities given their indices
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_path_and_cost():
    depot = 0
    min_tour = None
    min_cost = float('inf')
    
    # Import itertools to generate permutations of choices (one city from each group)
    from itertools import product
    
    # Generate all possible lists of city choices (one from each group)
    all_group_choices = list(product(*city_groups))
    
    # Check each possible combination of city choices
    for city_choices in all_group_choices:
        # Always start and end at the depot
        tour = [depot] + list(city_choices) + [depot]
        total_cost = 0
        
        # Calculate the total cost of the tour
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(tour[i], tour[i + 1])
        
        # Check if the found tour is better than the current best
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = tour
    
    return min_tour, min_cost

# Find the optimal tour path and its cost
optimal_tour, optimal_cost = find_path_and_cost()

print(f'Tour: {optimal_tour}')
print(f'Total travel cost: {optimal_cost:.2f}')