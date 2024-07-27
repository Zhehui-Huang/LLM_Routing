import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the shortest tour visiting exactly k cities starting and ending at the depot city
def find_shortest_k_tsp_tour(k):
    all_cities = list(cities.keys())
    best_tour = None
    best_cost = float('inf')
    
    # Consider all combinations of k-1 cities excluding the depot city
    for combo in itertools.combinations(all_cities[1:], k-1):
        selected_cities = [0] + list(combo)  # Always include the depot city

        # Consider all permutations of selected cities since it's a small number
        for perm in itertools.permutations(selected_cities[1:]):
            tour = [0] + list(perm) + [0]  # Start and end at the depot city
            cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
                
    return best_tour, best_cost

# Choose k as 5 to comply with the task requirements
tour, total_cost = find_shortest_k_tsp_tour(5)

# Output the solution as requested
print("Tour:", tour)
print("Total travel cost:", total_cost)