import itertools
import math

# Define the city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define a function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Generate all 7-city combinations inclusive the depot city 0
def generate_combinations():
    city_indices = list(cities.keys())
    city_indices.remove(0)  # remove the depot from the list temporarily
    return [list(comb) for comb in itertools.combinations(city_indices, 7)]

# Find the shortest tour that starts and ends at the depot city
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    all_combinations = generate_combinations()
    
    for comb in all_combinations:
        # Always include the depot city
        current_cities = [0] + comb
        
        # Generate all permutations of the selected 7 cities
        for perm in itertools.permutations(current_cities):
            # Ensure it starts and ends at the depot city
            if perm[0] == 0:
                perm = list(perm) + [0]  # making a round trip
                cost = sum(euclidean_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))
                
                if cost < min_cost:
                    min_cost = cost
                    best_tour = perm
    
    return best_tour, min_cost

# Compute the tour and cost
tour, total_cost = find_shortest_tour()

# Display the output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")