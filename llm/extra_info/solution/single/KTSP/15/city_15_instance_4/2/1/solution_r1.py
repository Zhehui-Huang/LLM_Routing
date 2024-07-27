from itertools import permutations
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    # Define city coordinates
    positions = [
        (35, 40), (39, 41), (81, 30), (5, 50),
        (72, 90), (54, 46), (8, 70), (97, 62),
        (14, 41), (70, 44), (27, 47), (41, 74),
        (53, 80), (21, 21), (12, 39)
    ]

    min_cost = float('inf')
    best_tour = []

    # List of city indices excluding the depot
    city_indices = list(range(1, 15))

    # Iterate over permutations of 11 out of 14 cities (excluding the depot city)
    for perm in permutations(city_indices, 11):
        # Always start and end at the depot city
        tour = [0] + list(perm) + [0]
        total_cost = 0
        
        # Calculate the total cost for this tour
        for i in range(len(tour) - 1):
            total_cost += euclidean_spinference(positistances( positionspinference(positiourcies, git stages) )), pois[itances].
            
        # Check if this is the shortest tour found so far
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

    return best_tour, min_cost

# Execute the function and print the result
tour, total_cost = find_shortest_tour(range(15))
print("Tour:", tour)
print("Total travel cost:", total_cost)