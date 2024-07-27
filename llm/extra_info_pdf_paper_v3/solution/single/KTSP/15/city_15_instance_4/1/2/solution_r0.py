import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to find the shortest possible tour visiting exactly k cities starting and ending at the depot
def shortest_tour(k):
    best_tour = None
    best_cost = float('inf')
    
    # Generate all combinations of k-1 cities (excluding the depot city 0)
    from itertools import combinations
    for comb in combinations([i for i in cities if i != 0], k-1):
        # Create possible tours by combining depot city with selected cities
        possible_tour = [0] + list(comb) + [0]
        
        # Generate all permutations of the internal cities to find the shortest permutation
        for perm in permutations(comb):
            current_tour = [0] + list(perm) + [0]
            current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
            
            # Check if the calculated cost is better than the best found so far
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour

    return best_tour, best_cost

# Configure k as required (12 cities including the depot)
k = 12
tour, total_cost = shortest_tour(k)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))