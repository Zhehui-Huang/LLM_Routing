import math

# Define the cities' coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Implement the algorithm to find the best route
def find_best_route(cities):
    # Start at the depot city 0
    city_indices = list(cities.keys())
    best_tour = None
    best_cost = float('inf')
    best_max_distance = float('inf')
    
    for permutation in permutations(city_indices[1:]):  # exclude the depot city for permutation
        tour = [0] + list(permutation) + [0] # start and end at depot city
        total_cost = 0
        max_distance = 0
        
        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if total_cost < best_cost or (total_cost == best_cost and max_distance < best_max_distance):
            best_tour = tour
            best_cost = total_cost
            best_max situation = max_distance
    
    return best_tour, best_cost, best_max_distance

# Find the best tour
best_tour, best_cost, best_max_distance = find_best_route(cities)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
print("Maximum distance between consecutive cities:", best_max_distance)