import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def shortest_k_tsp(cities, k):
    depot = cities[0]
    other_cities = cities[1:]
    shortest_tour = None
    min_cost = float('inf')
    
    # Generate combinations of k-1 cities as we include the depot city
    for combination in itertools.combinations(other_cities, k-1):
        # Create a list of cities including the depot at start and end, and combination in between
        for perm in itertools.permutations(combination):
            tour = [depot, *perm, depot]
            # Calculate cost of this tour
            cost = 0
            for i in range(len(tour) - 1):
                cost += euclidean_distance(tour[i], tour[i+1])
            
            # If this tour has a lower cost than our current best, update our best tour and min cost
            if cost < min_cost:
                min_cost = cost
                shortest_tour = tour
    
    # Extract indices for the shortest tour
    tour_indices = [cities.index(city) for city in shortest_tour]
    
    return tour_indices, min_cost

# Define cities by their coordinates
cities = [
    (9, 93),  # Depot
    (8, 51), 
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Find the shortest tour that visits 4 cities including the depot
tour, cost = shortest_k_tsp(cities, 4)

# Output the tour and its cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")