from itertools import combinations, permutations
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_shortest_tour(cities, k):
    depot = cities[0]
    city_indices = list(range(len(cities)))
    
    # Create all k-1 combinations of cities (excluding the depot)
    combos = list(combinations(city_indices[1:], k-1))
    shortest_distance = float('inf')
    best_tour = None
    
    for combo in combos:
        current_cities = [0] + list(combo)  # Always include the depot
        # Generate all permutations starting and ending at the depot
        for perm in permutations(current_cities[1:]):
            tour = [0] + list(perm) + [0]
            cost = total_tour_cost(tour, cities)
            if cost < shortest_distance:
                shortest_distance = cost
                best_tour = tour
                
    return best_tour, shortest_distance

# Define cities based on the given coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# We need to find the shortest tour that visits exactly 5 cities (including the depot)
shortest_tour, shortest_dist = find_shortest_tour(cities, 5)

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_dist}")