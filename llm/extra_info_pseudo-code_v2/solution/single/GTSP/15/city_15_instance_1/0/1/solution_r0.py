import math
import itertools

# City coordinates with city index as key
cities = {0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57), 6: (57, 30),
          7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)}

# City groups
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def evaluate_tour(tour):
    """ Calculate the total distance of the tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

def find_shortest_tour():
    """ Generate all possible tours and find the shortest one meeting the criteria """
    shortest_tour = None
    min_distance = float('inf')
    
    # Generate all combinations of one city from each group
    for combo in itertools.product(*groups):
        # Create a tour starting and ending at the depot (city 0), including one city from each group
        tour = [0] + list(combo) + [0]
        # Evaluate this tour
        current_distance = evaluate_tour(tour)
        # If this tour is shorter, update the shortest found so far
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = tour
            
    return shortest_tour, min_distance

# Finding the shortest tour
shortest_tour, min_distance = find_shortest_tour()

# Output results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance:.2f}")