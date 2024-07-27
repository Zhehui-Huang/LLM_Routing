import itertools
import math

# City coordinates indexed by city number
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate Euclidean distance between two cities 
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Brute-force search for the shortest 4-city tour
def find_shortest_tour():
    min_distance = float('inf')
    optimal_tour = []

    # Iterate over all combinations of 3 cities chosen from the 9 cities (excluding the depot)
    for combo in itertools.combinations(range(1, 10), 3):
        # Include the depot in the tour
        current_cities = [0] + list(combo)

        # Check all permutations of the selected cities to form cycles
        for perm in itertools.permutations(current_cities):
            if perm[0] == 0:  # Ensure tour starts with the depot
                # Calculate the cycle distance
                distance = sum(calculate_distance(perm[i], perm[(i+1) % len(perm)]) for i in range(len(perm)))
                
                # Update the optimal tour if this permutation gives a shorter distance
                if distance < min_distance:
                    min_distance = distance
                    optimal_took_and_back = list(perm) + [0]  # Append the depot to return
                    optimal_tour = optimal_took_and_back

    return optimal_tour, min_distance

# Execute the function and print the optimal tour and its cost
optimal_tour, min_distance = find_shortest_tour()
print(f'Tour: {optimal_tour}')
print(f'Total travel cost: {min_distance}')