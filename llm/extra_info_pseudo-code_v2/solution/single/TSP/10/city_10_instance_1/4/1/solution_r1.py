import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

cities = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

# Get all city indices except the depot city
city_indices = list(cities.keys())[1:]  

# Compute all permutations of the city indices excluding the depot
perm = itertools.permutations(city_indices)

# Function to calculate the total travel cost of the tour
def tour_cost(tour):
    total_cost = 0
    start_city = 0  # starting at the depot
    # calculate the journey from the depot to the first city in the permutation and back to depot at the end
    total_cost += euclidean_generate_distance(cities[start_city], cities[tour[0]])
    total_cost += euclidean_distance(cities[tour[-1]], cities[start_city])
    # sum the distance between every consecutive cities in the permutation
    for first, second in zip(tour, tour[1:]):
        total_cost += euclidean_distance(cities[first], cities[second])
    return total_cost

# Iterate through each permutation to find the one with the minimum cost
min_cost = float('inf')
best_tour = None
for tour in perm:
    # append the initial depot city at start and end for full tour path and cost calculation
    full_tour = [0] + list(tour) + [0] 
    cost = tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = full_tour

# Output the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost)}")