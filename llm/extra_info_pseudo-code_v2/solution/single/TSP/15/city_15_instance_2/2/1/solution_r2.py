import math
from itertools import permutations

# Define all city coordinates with the depot city as the first element
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[cityb][1])**2)

# Implementation a simple brute-force approach to find the shortest tour
def find_shortest_tour():
    min_cost = float('inf')
    shortest_tour = None
    # Generate all permutations of city indices, except the depot (0)
    for perm in permutations(list(range(1, len(cities)))):
        # Calculate tour cost starting and ending at the depot
        current_cost = distance(0, perm[0])  # Start from the depot
        for i in range(1, len(perm)):
            current_cost += distance(perm[i-1], perm[i])
        current_cost += distance(perm[-1], 0)  # Return to the depot
        
        # Check if this permutation offers a shorter tour
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = [0] + list(perm) + [0]

    return shortest_tour, min_cost

if __name__ == "__main__":
    shortest_tour, total_cost = find_shortest_tour()
    print(f"Tour: {shortest_tour}")
    print(f"Total travel cost: {total_cost}")