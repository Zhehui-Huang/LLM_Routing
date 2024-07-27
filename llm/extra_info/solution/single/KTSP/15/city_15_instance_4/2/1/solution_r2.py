from itertools import permutations
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour():
    # Define city coordinates
    positions = [
        (35, 40), (39, 41), (81, 30), (5, 50),
        (72, 90), (54, 46), (8, 70), (97, 62),
        (14, 41), (70, 44), (27, 47), (41, 74),
        (53, 80), (21, 21), (12, 39)
    ]

    min_cost = float('inf')
    best_tour = None

    # Iterate over combinations of 11 cities (excluding the depot, which is city 0)
    city_indices = list(range(1, 15))  # indices of the other cities

    for perm in permutations(city_indices, 11):
        # Calculate tour starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        total_cost = 0
        
        # Compute the total cost of this tour
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(positions[tour[i]], positions[tour[i + 1]])
        
        # Update the best found tour if the current one has a lower cost
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

    return best_tour, min_cost

# Run the function and output the result
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)