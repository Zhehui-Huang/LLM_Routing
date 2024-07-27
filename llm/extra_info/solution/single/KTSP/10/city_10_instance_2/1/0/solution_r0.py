import itertools
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Utility function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Searching for the shortest tour visiting exactly 6 cities
def find_shortest_tour():
    # Depot city is always included
    depot = 0
    all_cities = set(cities.keys()) - {depot}

    # Best tour starts with an infinitely large cost
    min_cost = float('inf')
    best_tour = None

    # Generate all combinations of 5 cities from the remaining cities (excluding the depot)
    for combo in itertools.combinations(all_cities, 5):
        # Create possible tours by visiting chosen cities and returning to the depot
        for perm in itertools.permutations(combo):
            tour = [depot] + list(perm) + [depot]

            # Calculate the total cost of this tour
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += euclidean_distance(tour[i], tour[i+1])
            
            # Check if this tour is better than the currently known best tour
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = tour
    
    return best_tour, min_cost

# Find the optimal tour and its cost
tour, total_cost = find_shortest_tour()

# Output the result in required format
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))