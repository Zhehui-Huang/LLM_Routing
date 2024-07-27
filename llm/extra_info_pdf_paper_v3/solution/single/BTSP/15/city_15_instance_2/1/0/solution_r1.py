import math

# City positions indexed by city numbers
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
# Generate all permutations of city visits
num_cities = len(cities)
permutations_cities = permutations(range(1, num_cities))  # excluding the depot city 0 for permutation

min_max_distance = float('inf')
best_tour = None

# Evaluate each permutation
for perm in permutations_cities:
    # Create the full route by adding the depot at the start and the end
    full_route = [0] + list(perm) + [0]
    
    # Calculate the total travel cost and the maximum distance in the current route
    total_cost = 0
    max_distance = 0
    
    for i in range(len(full_route) - 1):
        dist = euclidean_distance(full_route[i], full_route[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
            
    # Check if this route is better according to the maximum distance criterion
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = full_route

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")